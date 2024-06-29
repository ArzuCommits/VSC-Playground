import java.util.Scanner;

class BubbleSort 
{
    public static void main(String[] args) 
    {
        Scanner a = new Scanner(System.in);
        System.out.print("Enter a number to select the range of your array: ");
        int n = a.nextInt();
        int[] ar = new int[n];
        for (int i = 0; i < n; i++) {
            System.out.print("Enter element " + i + ": ");
            ar[i] = a.nextInt();
        }
        System.out.print("Array elements: ");
        for (int i : ar)
            System.out.print(i + " ");
        
        System.out.println("\nSorted array: ");
        for(int i = 0 ; i < n-1 ; i++)
        {
            for(int j = 0 ; j < n-1-i ; j++)
            {
                if(ar[j] > ar[j+1])
                {
                    int t = ar[j];
                    ar[j]=ar[j+1];
                    ar[j+1]=t;
                }
            }
        }

        for(int i: ar)
        System.out.print(i+" ");

        a.close();
    }
}
