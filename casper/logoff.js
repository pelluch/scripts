
// This will hold all of the content that Casper needs to supply.
var config = {
	url: 'http://192.168.1.1'
};

casper.start(config.url, function() {
	// this.echo(this.getTitle());
	this.fill('form#authform', { user: 'user', password: 'admin' }, 
false);
	this.click('input[name="ok"]');
});

casper.then(function() {
	this.click('input[name="13"]');
});

casper.run();
