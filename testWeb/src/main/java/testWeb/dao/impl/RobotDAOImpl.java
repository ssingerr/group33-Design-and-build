package testWeb.dao.impl;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import testWeb.dao.RobotDAO;
import testWeb.db.DBConnect;
import testWeb.vo.RobotInfo;
import java.util.Base64;

public class RobotDAOImpl implements RobotDAO{

	@Override
	public List<RobotInfo> queryBymessageInfo(RobotInfo robotInfo) throws Exception {
		// TODO Auto-generated method stub
		List<RobotInfo> strings= new ArrayList<>();	
		String sql ="select * from robot where username=?";
		PreparedStatement pstmt =null;
		DBConnect dbc=null;
		
		
		
		try {
			dbc =new DBConnect();
			pstmt = dbc.getConnection().prepareStatement(sql);
			pstmt.setString(1,robotInfo.getUsername());
			
			ResultSet rs =pstmt.executeQuery();		
			while(rs.next()) {
				RobotInfo robotinfo1 = new RobotInfo();
				robotinfo1.setnumber(rs.getString("time"));
				robotinfo1.setUsername(rs.getString("username"));
				robotinfo1.setimage(rs.getString("image"));
				strings.add(robotinfo1);
				//String number=rs.getString("number");;
				//strings.add(number);
				
			}
			rs.close();
			pstmt.close();
			
		}catch(SQLException e) {
			System.out.println(e.getMessage());
		}finally {
			dbc.close();
			}
		  return strings;
	}
	
	

}
