

X (Avg Sales Per State) = CALCULATE(AVERAGE('Customer List'[Last 6 Months Purchases]), ALLEXCEPT ( 'Regression Table', 'Regression Table'[State] ))
X_SQUARED = [X (Avg Sales Per State)] ^ 2
Y_SQUARED = [Y (Avg Income Per State)] ^ 2 
XY = [X (Avg Sales Per State)] * [Y (Avg Income Per State)]
n = COUNTROWS('Regression Table')
Sum_X = SUM('Regression Table'[X (Avg Sales Per State)])
Sum_Y = SUM('Regression Table'[Y (Avg Income Per State)])
Sum_X_SQUARED = SUM('Regression Table'[X_SQUARED])
Sum_Y_SQUARED = SUM('Regression Table'[Y_SQUARED])
Sum_XY = SUM('Regression Table'[XY])
b = DIVIDE([Sum_Y]*[Sum_X_SQUARED]-[Sum_X]*[Sum_XY],[n]*[Sum_X_SQUARED]-[Sum_X]^2)
m = DIVIDE([n]*[Sum_XY]-[Sum_X]*[Sum_Y],[n]*[Sum_X_SQUARED]-[Sum_X]^2)
Final Formula = "y = "&ROUND([m],2)&"X+ "&ROUND([b],2)

