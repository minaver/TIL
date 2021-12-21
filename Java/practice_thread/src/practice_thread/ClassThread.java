package practice_thread;

public class ClassThread extends Thread{
	
	private int[] temp;
	
	public ClassThread(String threadname) {
		super(threadname);
		temp = new int[10];
		
		for(int start=0;start<temp.length;start++)
			temp[start] = start;
	}
	
	public void run() {
		for(int start:temp) {
			try {
				Thread.sleep(1000);
			} catch(InterruptedException ie){
				ie.printStackTrace();
				// TODO : handle exception
			}
			System.out.println("스레드이름 : "+currentThread().getName());
			System.out.println("temp value : "+start);
		}
	}
	
	public static void main(String[] args) {
		ClassThread ct = new ClassThread("thread1");
		ClassThread ct2 = new ClassThread("thread2");
		
		ct.start();
		ct2.start();
	}

}
