package main.java.interactome.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;

import main.java.interactome.domain.Link;
import main.java.interactome.domain.Node;
import main.java.interactome.DAO.InteractomeDAO;;


public class InteractomeService{
	private InteractomeDAO interactomeDAO = new InteractomeDAO();
	
	public List<Link> getInteractomeData(List<Node> nodes){
		List<Link> links = interactomeDAO.getInteractomeData(nodes);
		
		return links;
	}
	
	
}