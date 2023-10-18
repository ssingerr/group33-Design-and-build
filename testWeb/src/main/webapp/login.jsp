<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Welcome to ROBOT System</title>
<link rel="stylesheet" type="text/css" href="login.css">
</head>
<body>
   <div class="form-div">
   <div class="reg-content">
   <h1>Welcome </h1>
   <span>Haven't your account？</span>
    <button onclick="redirectToRegistrationPage()">register</button>
  <script>
    function redirectToRegistrationPage() {
      // 跳转到注册页面
      window.location.href = "register.jsp";
    }
  </script>
  

   </div>
  <form id ="reg-form" method="post" action="./login">
  <table>
    <tr>
    <tb class="inputs">
     <label for="username">Username：</label>
    <input type="text" id="username" name="username">
      </tb>
      </tr>
    
    <tr>
    <tb class="inputs">
    <label for="password">Password：</label>
    <input type="text" id="password" name="password">
      </tb>
      </tr>
 </table>
 <div class="buttons">
      <input type="submit" id="submit" value="Submit">
    </div>
   <br class="clear">
   </form>
  </div>
</body>
</html>