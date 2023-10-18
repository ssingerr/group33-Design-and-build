package testWeb.dao.impl;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Base64;
import java.util.List;

import testWeb.dao.UserDAO;
import testWeb.db.DBConnect;
import testWeb.vo.UserInfo;

public class UserDAOImpl implements UserDAO {

	public int queryByUserInfo(UserInfo userinfo) throws Exception {
		int flag = 0;
		String sql = "select * from userinfo where username=?";
        PreparedStatement pstmt = null ;   
        DBConnect dbc = null;   
  
        // 下面是针对数据库的具体操作   
        try{   
            // 连接数据库   
            dbc = new DBConnect() ;   
            pstmt = dbc.getConnection().prepareStatement(sql) ; 
            pstmt.setString(1,userinfo.getUsername()) ;   
            // 进行数据库查询操作   
            ResultSet rs = pstmt.executeQuery();
            while(rs.next()){  
                // 查询出内容，将其与用户提交的内容对比 
                if(rs.getString("password").equals(userinfo.getPassword())){
                	flag = 1;
                } 
            }   
            rs.close() ; 
            pstmt.close() ;   
        }catch (SQLException e){   
            System.out.println(e.getMessage());   
        }finally{   
            // 关闭数据库连接   
            dbc.close() ;   
        }   
		return flag;
	}
	public int registerUser(UserInfo userinfo) throws Exception {
	    int flag = 0;
	    String sql = "INSERT INTO userinfo (username, password) VALUES (?, ?)";
	    PreparedStatement pstmt = null;
	    DBConnect dbc = null;

	    try {
	        dbc = new DBConnect();
	        pstmt = dbc.getConnection().prepareStatement(sql);
	        pstmt.setString(1, userinfo.getUsername());
	        pstmt.setString(2, userinfo.getPassword());

	        int rowsAffected = pstmt.executeUpdate();
	        if (rowsAffected > 0) {
	            flag = 2; // Registration successful
	        }
	    } catch (SQLException e) {
	        System.out.println(e.getMessage());
	    } finally {
	        dbc.close();
	    }
	    return flag;
	}
	@Override
	public int queryByUserInfo1(UserInfo var1) throws Exception {
		// TODO Auto-generated method stub
		return 0;
	}
	@Override
	public int queryByUserInfo2(UserInfo var1) throws Exception {
		// TODO Auto-generated method stub
		return 0;
	}
	@Override
	public int queryByUserInfo4(UserInfo var1) throws Exception {
		// TODO Auto-generated method stub
		return 0;
	}
	@Override
	public String queryByUserInfo3(UserInfo var1) throws Exception {
		// TODO Auto-generated method stub
		return null;
	}
}