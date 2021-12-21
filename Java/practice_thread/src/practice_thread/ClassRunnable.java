package practice_thread;

public class ClassRunnable implements Runnable {
	
	private int index;
	
	public ClassRunnable() {
		
	}
	
	public ClassRunnable(int index) {
		this.index = index;
		//setName("no name");
	}
	
	@Override
	public void run() {
		
			try {
				Thread.sleep(2000);
			} catch(InterruptedException ie) {
				ie.printStackTrace();
			}
		
		
		System.out.println("스레드이름 : "+Thread.currentThread().getName());
		System.out.println(Thread.currentThread().getName()+" ID : "+Thread.currentThread().getId());
	}
	
	public static void main(String[] args) {
		
		Thread mainThread = Thread.currentThread();
		System.out.println("main Thread Name : "+mainThread.getName());
		System.out.println("main Thread ID : "+mainThread.getId());

		
		ClassRunnable cr = new ClassRunnable();
		Thread t1 = new Thread(cr,"firstThread");
		Thread t2 = new Thread(cr,"secondThread");
		Thread t3 = new Thread(new ClassRunnable(3));
		
		t1.start();
		try {
			t1.join();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		t2.start();
		try {
			t2.join();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		t3.start();
	}
}
