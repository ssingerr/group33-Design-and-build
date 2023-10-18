<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>SUCCESS</title>
</head>
<body>
   <%String username = (String)session.getAttribute("username"); %>
    welcome   <%= username %>
    
   <div id="subDiv">
		<a href="./login.jsp">back to login</a>
	</div>

</body>
</html>