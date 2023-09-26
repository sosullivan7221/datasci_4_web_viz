#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

# Libraries
library(shiny)
library(dplyr)
library(ggplot2)
library(rsconnect)

# UI 
ui <- fluidPage(
  titlePanel("Adults Sleeping less than 7 Hours Nightly Age-adjusted Prevalence in MA by County"),
  sidebarLayout(
    sidebarPanel(
      selectInput("county", "Choose a county:", choices = NULL)
    ),
    mainPanel(
      plotOutput("barPlot")
    )
  )
)


# Server logic
server <- function(input, output, session) {
  
  # Dataest
  df <- reactive({
    path <- "https://raw.githubusercontent.com/sosullivan7221/datasci_4_web_viz/main/dataset/massachusetts_data.csv"
    read.csv(path)
  })
 
  # Filter the dataset
  df_sleep <- reactive({
    data <- df()
    filter(data, MeasureId == "SLEEP", Data_Value_Type == "Age-adjusted prevalence")
  })

  # Update county choices dynamically based on dataset
  observe({
    sleep_data <- df_sleep()
    updateSelectInput(session, "county", choices = sort(unique(sleep_data$LocationName)))
  })
  
  # Render the bar plot
  output$barPlot <- renderPlot({
    sleep_data <- df_sleep()
    county_data <- sleep_data[sleep_data$LocationName == input$county, ]
    avg_value <- mean(sleep_data$Data_Value, na.rm = TRUE)
    
    ggplot() +
      geom_bar(data = county_data, aes(x = LocationName, y = Data_Value, fill = LocationName), stat = "identity") +
      geom_hline(aes(yintercept = avg_value), linetype = "dashed", color = "dodgerblue") +
      labs(title = 'Adults Sleeping less than 7 Hours Nightly Age-adjusted Prevalence',
           y = 'Data Value (Age-adjusted prevalence) - Percent',
           x = 'Location (County)') +
      theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
      ylim(0, 30) +
      scale_fill_manual(values = c("lightcoral", "dodgerblue"))
  })
  
  }

# Run the application 
shinyApp(ui = ui, server = server)
