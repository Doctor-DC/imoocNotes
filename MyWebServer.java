import java.io.*;
import java.net.*;
public class MyWebServer
{
    public static void main(String []args) throws Exception{
        
        ServerSocket ss=new ServerSocket(80);
    
            Socket s=ss.accept();
            System.out.println("wait in 9999");
            OutputStream os=s.getOutputStream();
            BufferedReader br=new BufferedReader(new FileReader("f://hello.html"));
			System.out.println("output");
            String buf="";
            while((buf=br.readLine())!=null){
                os.write(buf.getBytes());
            }
        br.close();
        os.close();
        s.close();
        

    }
}