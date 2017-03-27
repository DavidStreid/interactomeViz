package main.java.interactome.domain;

//NODE: {"id": "1", "label": "MDFI"}

public class Node {
	private String id;
	private String label;
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getLabel() {
		return label;
	}
	public void setLabel(String label) {
		this.label = label;
	}
	
	public Node(String id, String label){
		this.id = id;
		this.label = label;
	}
}