import java.util.*;
public class Deletion 
{
    public static void main(String args[])
    {
        Scanner a = new Scanner(System.in);
        System.out.print("\nEnter a number to declare the range of the array: ");int n = a.nextInt();
        int ar[] = new int[n+1];

        for(int i = 0 ; i < n ; i++)
        {
            System.out.print("\nEnter a number in index: " + i + ": ");
            ar[i] = a.nextInt();
        }
        
        System.out.print("\nEnter the position from where you want to delete an element: ");int pos = a.nextInt();

        for(int i = pos-1 ; i < n ; i++)
        {
           ar[i] = ar[i+1] ;
        }

        System.out.println("Required array: ");
        for(int i = 0 ; i < n ; i ++)
        System.out.print(ar[i]+" ");

        a.close();

    }
}
