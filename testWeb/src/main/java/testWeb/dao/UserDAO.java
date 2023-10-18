package testWeb.dao;

import java.util.List;

import testWeb.vo.UserInfo;

public interface UserDAO {
    public int queryByUserInfo(UserInfo userinfo) throws Exception;
    
    public int registerUser(UserInfo userinfo) throws Exception;

    int queryByUserInfo1(UserInfo var1) throws Exception;

    int queryByUserInfo2(UserInfo var1) throws Exception;

    int queryByUserInfo4(UserInfo var1) throws Exception;

    String queryByUserInfo3(UserInfo var1) throws Exception;
}


