package main.java.interactome.domain;

//LINK: {"source": "5", "target": "3"}

public class Link{
	private String source;
	private String target;
	
	public Link(String source, String target){
		this.source = source;
		this.target = target;
	}
	
	public String getSource() {
		return source;
	}
	public void setSource(String source) {
		this.source = source;
	}
	public String getTarget() {
		return target;
	}
	public void setTarget(String target) {
		this.target = target;
	}
}