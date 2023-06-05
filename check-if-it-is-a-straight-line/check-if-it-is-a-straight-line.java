class Solution 
{
    public boolean checkStraightLine(int[][] coordinates) 
    {
		double slope = (double)(coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0]);
		boolean lieOnLine = true;
		
		for(int i=2;i<coordinates.length;i++)
		{

			  int x0 = coordinates[0][0];
        int y0 = coordinates[0][1];
        int x1 = coordinates[1][0];
        int y1 = coordinates[1][1];
				int x  = coordinates[i][0];
        int y  = coordinates[i][1];

			      double currentSlope = (double)(coordinates[i][1] - coordinates[0][1]) / (coordinates[i][0] - coordinates[0][0]);
			
			 if ((x - x0) * (y1 - y0) - (y - y0) * (x1 - x0) != 0) {
                lieOnLine = false;
                break;
            }
		   }
			 return lieOnLine;
		}
}

	  