class Solution 
{
    public boolean checkStraightLine(int[][] coordinates) 
    {
        // double slope = (coordinates[0][0]-coordinates[1][0])/(coordinates[0][1]-coordinates[1][1]);
		
		boolean lieOnLine = true;
		
		for(int i=2;i<coordinates.length;i++)
		{
			// double currSlope = (coordinates[0][1] - coordinates[i][1]) / (double) (coordinates[0][0] - coordinates[i][0]);
				if((coordinates[1][0] - coordinates[0][0]) * (coordinates[i][1] - coordinates[0][1]) != (coordinates[1][1] - coordinates[0][1]) * (coordinates[i][0] - coordinates[0][0]))
				{
					lieOnLine = false;
					break;
				}
		   }
			 return lieOnLine;
		}
}

	  