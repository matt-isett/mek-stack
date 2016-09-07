# The MEK Stack!  Metricbeat - Elasticsearch - Kibana
	This is a docker-compose based deployment for the three products for the 5.0 release.  
	There are some cool features like Metricbeat product, kibana dashboards, security, 
	and watches that a user can experiment with.

# Git Submodules
	This project uses submodules so when you clone use *git clone --recursive*
		
# Usage

	make initial-run
		Wait for a few kibana log lines to end, less then 1-2 mins, then Ctrl-C to stop.
	make run-mek-stack

	Log into Kibana at Docker default IP:9200 with elastic and changeme
