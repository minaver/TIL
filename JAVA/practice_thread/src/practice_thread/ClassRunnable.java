package practice_thread;

public class ClassRunnable implements Runnable {
	
	private int[] temp;
	
	public ClassRunnable() {
		temp = new int[10];
		
		for(int start=0;start<temp.length;start++)
			temp[start] = start;
	}
	
	@Override
	public void run() {
		
		for (int start:temp) {
			try {
				Thread.sleep(2000);
			} catch(InterruptedException ie) {
				ie.printStackTrace();
			}
		
		
		System.out.println("스레드이름 : "+Thread.currentThread().getName());
		System.out.println("스레드ID : "+Thread.currentThread().getId());
		System.out.println("temp value : "+start);
		}
	}
	
	public static void main(String[] args) {
		ClassRunnable cr = new ClassRunnable();
		Thread t = new Thread(cr,"firstThread");
		
		t.start();
	}
}
