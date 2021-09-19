package prac_protected;

import java_practice.*;

public class Class_test4 extends Class_test2{ // practice use protected field 
	
	public Class_test4(String name, int pay, String dept){
		super(name,pay,dept);
	}

	void printName() { // use protected field in inheritance class in diff module 
		System.out.println(name+dept); // if private name, dept -> The field Class_test2.dept is not visible
	}
	
	
	public static void main(String[] args) {
		Class_test4 test4 = new Class_test4("chun-sik",4000,"front-end");
		
		System.out.println(test4.name); // if private name -> The field Class_test2.name is not visible
		System.out.println(test4.pay);
		System.out.println(test4.dept);
	}
}
