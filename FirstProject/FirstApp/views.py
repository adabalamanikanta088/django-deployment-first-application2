from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def hello(request): #view-function
	#ss ----> is html-data/code
    ss = '''
    <html>
	<head>
		<title>***Welcome-Page***</title>
	</head>
    <style>
        h1{
            color:Blue;
            width:95%;
        }
        h1{
        background-color:Red
        }
        h2{
            color:Green;
            width:75%; 
    </style>
	<body>
		<center>
			<h1>Welcome to DJANGO HTML webpage</h1>
			<hr color="brown" width="95%"/>
			<h2>Welcome to DJANGO HTML webpage</h2>
			<hr color="brown" width="85%"/>
			<h3>Welcome to DJANGO HTML webpage</h3>
			<hr color="brown" width="75%"/>
			<h4>Welcome to DJANGO HTML webpage</h4>
			<hr color="brown" width="65%"/>
			<h5>Welcome to DJANGO HTML webpage</h5>
			<hr color="brown" width="55%"/>
			<h6>Welcome to DJANGO HTML webpage</h6>
			<hr color="brown" width="45%"/>
		</center>
	</body>
</html>
		''';
        
    return HttpResponse(ss);
    
    
import time;
def senddatetime(request):
    ct=time.ctime()
    ss='''
    <html>
    <head>
        <title>Date-time Request</title>
    <style>
    h1{
        color:blue;
        width:97%;
    }
    h2{
        color:Red;
        width:85%;
    }
    </style>
    </head>
    <body>
        <center>
        <h1>Welcome to python class</h1>
        <hr color:"Yello" width:"95%"
        <h2>''',ct,'''</h2>
        <hr color:"Red" width:"85%"
        </center>
    </body>
    
    
    </html>
        ''';
    
    return HttpResponse(ss)








