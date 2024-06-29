import java.util.*;
public class Inserting 
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
        
        System.out.print("\nEnter the number you want to fit in the array: ");int num = a.nextInt();
        System.out.print("\nEnter the position where you want to fit in the mentioned element: ");int pos = a.nextInt();

        for(int i = n ; i >= pos ; i--)
        {
            int t = ar[i];
            ar[i] = ar[i-1];
            ar[i-1] = t;
        }

        ar[pos-1] = num;
        System.out.println("Required array: ");
        for(int i: ar)
        System.out.print(i+" ");

        a.close();
    }
}
