package testWeb.servlet;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import testWeb.vo.UserInfo;
import testWeb.dao.UserDAO;
import testWeb.dao.impl.UserDAOImpl;

public class UserRegisterServlet extends HttpServlet {

    public void doGet(HttpServletRequest req, HttpServletResponse res)
        throws IOException, ServletException {
        doPost(req, res);
    }

    public void doPost(HttpServletRequest req, HttpServletResponse res)
        throws IOException, ServletException {
        UserInfo userinfo = new UserInfo();
        userinfo.setUsername(req.getParameter("username"));
        userinfo.setPassword(req.getParameter("password"));

        UserDAO dao = new UserDAOImpl();
        int flag = 0;
        try {
            flag = dao.registerUser(userinfo);
        } catch (Exception e) {
            e.printStackTrace();
        }

        if (flag == 2) {
            HttpSession session = req.getSession();
            session.setAttribute("username", userinfo.getUsername());
            res.sendRedirect("./success.jsp");
        } else {
            res.sendRedirect("./fail.jsp");
        }
    }
}

