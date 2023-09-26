# datasci_4_web_viz
Data visualization using shiny r, shiny python, and python flask

## Shiny R

Had an issue with certain data points not showing up, with the console saying rows with missing values were removed. This is because the values fell outside of the axis range. This was not an issue in shiny python, where the values greater than the axis were displayed but you could not see the entire bar. Adjusting the axis range to be greater allowed all values to be shown.

Link: https://sosullivan.shinyapps.io/mass-app/

## Shiny Python

Had initial issues with the requirements.txt file, as shiny was pip-freezing the Google shell environment, and the 200+ packages shell has installed were causing a number of issues due to version numbers. I wrote my own requirements.txt but it didn't read it so I just switched to VSCode to work locally and had no issues.

Link: https://sosullivan.shinyapps.io/mass-data-app/

## Python Flask

No issues here really, deployed smoothly.
