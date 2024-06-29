import java.util.*;

public class BInarySearch 
{
    public static void main(String args[]) {
        Scanner a = new Scanner(System.in);
        System.out.print("Enter a number to decide the range of the array: ");
        int n = a.nextInt();
        int ar[] = new int[n];

        for (int i = 0; i < n; i++) {
            System.out.print("\nEnter a number in index: " + i + ": ");
            ar[i] = a.nextInt();
        }

        Arrays.sort(ar);

        System.out.print("\nEnter an element you eant to search: ");int num = a.nextInt();

        int mid = 0, last = n, start = 0;
        boolean flag = false;

        while(start <= last)
        {
            mid = (last + start)/2;

            if(ar[mid] == num)
            {
                flag = true;
                break;
            }
            else if(ar[mid] > num)
            {
                last = mid - 1;
            }
            else if(ar[mid] < num)
            {
                start = mid + 1;
            }

        }
        if(flag)
        System.out.println(num+" is found in "+mid+" index.");
        else
        System.out.println(num+" is not found in the folloiwng array.");
        a.close();
    }

    
}
