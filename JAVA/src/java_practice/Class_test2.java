package java_practice;

public class Class_test2 extends Class_test1 {
	
	private String	dept;
	
	public String getDept() {
		return dept;
	}
	
	public Class_test2(String name, int pay, String dept){
		this.name = name;
		this.pay = pay;
		this.dept = dept;
	}
	
	void getInformation(){ 
		System.out.println("Name : "+ this.name + " Pay : "+this.pay+ " Department : "+this.dept);
	}
	
	void prn(){
		System.out.println("sub-class");
	}
}
