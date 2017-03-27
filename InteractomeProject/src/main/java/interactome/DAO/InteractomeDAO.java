package main.java.interactome.DAO;

import java.util.ArrayList;
import java.util.List;

import main.java.interactome.domain.Link;
import main.java.interactome.domain.Node;

public class InteractomeDAO{
	public List<Link> getInteractomeData(List<Node> nodes){
		List<Link> links = new ArrayList<Link>();
		
		links.add(new Link("5", "3"));
		links.add(new Link("3", "4"));
		links.add(new Link("4", "5"));
		return links;
	}
}