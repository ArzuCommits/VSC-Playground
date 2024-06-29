import java.util.*;
class Piglatin 
{

    public static boolean isVowel(char ch)
    {
        Character.toLowerCase(ch);
        if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    public static void main(String args[])
    {
        Scanner a = new Scanner(System.in);

        System.out.print("Enter a word to convert it into piglatin: "); String st = a.next();
        String con = "", pig = "";

        for(int i = 0 ; i < st.length() ; i++)
        {
            if(isVowel(st.charAt(i)))
            {
                con = st.substring(0, i);
                pig = st.substring(i) + con + "ay";
                break;
            }
        }
        String piglatin = (pig == "") ? (st+"ay") : (pig);
        System.out.println("Piglatin word is: "+piglatin);
        a.close();
    }
}
