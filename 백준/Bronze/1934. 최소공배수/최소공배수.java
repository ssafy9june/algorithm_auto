import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main (String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		for (int i=0; i<n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			if (a < b) {
				int tmp = a;
				a = b;
				b = tmp;
			}
			int r = 1;
			int aa = a;
			int bb = b;
			while (bb!=0) {
				r = aa % bb;
				aa = bb;
				bb = r;
			}
			System.out.println(a*b/aa);
		}
	}
}