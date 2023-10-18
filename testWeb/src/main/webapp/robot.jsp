<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%@ page import="testWeb.vo.RobotInfo" %>
    <%@ page import="java.util.ArrayList" %>
    <%@ page import="java.util.List" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>INFORMATION</title>
  <link rel="stylesheet" type="text/css" href="Robot.css">
</head>
<body>
    <table>
        <tr>
            
            <th>Username</th>
            <th>time</th>
            <th>image</th>
        </tr>

        
        <% List<RobotInfo> rob = (List<RobotInfo>) session.getAttribute("rob");
               if (rob != null && !rob.isEmpty()) {
               for (RobotInfo robot : rob) {
               String username = robot.getUsername();
               String time = robot.getnumber();
               String image = robot.getimage();
    %>
    <tr>
        <td><%= username %></td>
        <td><%= time %></td>
         <td class="centered"><img src="<%= image %>" /></td> <!-- 应用样式类来居中图像 -->
    </tr>
    <%}} %>

        
    </table>
</body>
</html>
