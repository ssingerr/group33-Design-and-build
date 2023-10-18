package testWeb.dao;

import java.util.List;

import testWeb.vo.*;

public interface RobotDAO {
	public List<RobotInfo> queryBymessageInfo(RobotInfo robotInfo) throws Exception;
		
	}