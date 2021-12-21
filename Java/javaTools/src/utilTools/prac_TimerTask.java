package utilTools;

import java.util.Timer;
import java.util.TimerTask;

public class prac_TimerTask {
	public static void main(String[] args) {
		
		Timer timer = new Timer();
		TimerTask ts = new TimerTask() {		
			
			@Override 
			public void run() {
						System.out.println("done!");
			}
		
		};
		timer.schedule(ts,1000,1000);
	}
}

