package practice_thread;

public class ClassAnonyRunnable {
	public static void main(String[] args) {
		
		
// make thread object t1 
		Thread t1 = new Thread(new Runnable() {
			@Override
			public void run() {
				try {
					Thread.sleep(1000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				System.out.println("[ t1 ]Thread name : "+Thread.currentThread().getName()+" || Thread ID : "+ Thread.currentThread().getId());
			}
		});
	
// make no name thread object(can't reuse)
		 new Thread(new Runnable() {
			@Override
			public void run() {
				try {
					Thread.sleep(1000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				System.out.println("[ No reuse ] Thread name : "+Thread.currentThread().getName()+" || Thread ID : "+ Thread.currentThread().getId());
			}
		}).start();
		 
//main thread
		 try {
			Thread.sleep(3000);
		} catch (InterruptedException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		 System.out.println(Thread.currentThread().getName() + " : Am i first one?");
		 
// make anonymous thread
		 new Thread(() ->{
			 System.out.println("[ Anonymous1 ] Thread name : "+Thread.currentThread().getName()+" || Thread ID : "+ Thread.currentThread().getId());
		 }).start();
		 
		Thread t_anony = new Thread(() -> System.out.println("[ Anonymous2 ] Thread name : "
				+Thread.currentThread().getName()+" || Thread ID : "+ Thread.currentThread().getId()) );
		
		t_anony.start();
		try {
			t_anony.join();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
// main thread
		//System.out.println(Thread.currentThread().getName() + " : Am i first one?");
		
		t1.start();

		
		
	}
}
