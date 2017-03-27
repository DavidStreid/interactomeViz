package main.java.interactome.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import main.java.interactome.service.InteractomeService;

import main.java.interactome.domain.Link;
import main.java.interactome.domain.LinkRequest;
import main.java.interactome.domain.Node;

@RestController
public class InteractomeController {
	// NOTE - AutoWiring is for when you have another project (WITH A POM) that is a dependency
	private InteractomeService interactomeService = new InteractomeService();
	
	@RequestMapping("/getLinks")
	public List<Link> getLinks(@RequestBody LinkRequest linkRequest) {
		List<Node> nodes = linkRequest.getNodes();
		
		List<Link> links = interactomeService.getInteractomeData(nodes);
		return links;
	}
}
