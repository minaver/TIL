package java_practice;

public class inheritance {
	public static void main(String args[]) {
		Class_test1 test1 = new Class_test1();
		Class_test2 test2 = new Class_test2("ryan",6000,"back-end");
		
		test1.prn();
		test2.prn();
		test2.getInformation();
		
		System.out.println(test2.name);
		
	}
}
