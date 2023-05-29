import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int hr = Integer.parseInt(st.nextToken());
		int mn = Integer.parseInt(st.nextToken());
		int sc = Integer.parseInt(st.nextToken());
		int add = Integer.parseInt(br.readLine());
		int time = hr*3600 + mn*60 + sc + add;
		int nhr = time / 3600;
		int nmn = (time % 3600) / 60;
		int nsc = time % 60;
		if (nhr > 23){
			nhr = nhr % 24;
		}
		System.out.println(nhr + " " + nmn + " " + nsc);
		}
}