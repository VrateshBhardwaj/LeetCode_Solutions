class Solution 
{
    public boolean checkStraightLine(int[][] coordinates) 
    {
			
		boolean lieOnLine = true;
		
		for(int i=2;i<coordinates.length;i++)
		{

			      int x1 = coordinates[0][0];
            int y1 = coordinates[0][1];
            int x2 = coordinates[1][0];
            int y2 = coordinates[1][1];
            int x  = coordinates[i][0];
            int y  = coordinates[i][1];
			
				if((x2 - x1) * (y - y1) != (y2 - y1) * (x - x1))
				{
					lieOnLine = false;
					break;
				}
		   }
			 return lieOnLine;
		}
}

	  