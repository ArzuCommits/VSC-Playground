import java.util.*;
class Merge 
{
    public static void main(String []args) 
    {
        Scanner a=new Scanner(System.in);
        System.out.print("\nEnter a number to declare the size of the first array: ");int n = a.nextInt();
        System.out.print("\nEnter a number to declare the size of the second array: ");int m = a.nextInt();
        
        int ar1[] = new int[n], ar2[] = new int[m], ar3[] = new int[n+m];

        System.out.println("Enter array elements in 1st array: ");
        for(int i = 0 ; i < n ; i++)
        ar1[i]=a.nextInt();

        System.out.println("Enter array elements in 2nd array: ");
        for(int i = 0 ; i < m ; i++)
        ar2[i]=a.nextInt();

        int x=0,y=0;

        System.out.println("Required array:");
        for(int i = 0 ; i < n+m ; i++)
        {
            if(i<n)
            ar3[i] = ar1[x++];
            else 
            ar3[i] = ar2[y++];
        }

        for(int i = 0 ; i < m+n ; i++)
        System.out.print(ar3[i]+" ");
        a.close();
    }
}