describe('DecapCMS Integration', () => {
	it('should load the CMS login page', () => {
	  cy.visit('/admin');
	  cy.contains('Login').should('be.visible');
	});

	it('should allow a user to log in', () => {
	  cy.visit('/admin');
	  cy.get('input[name="email"]').type('david.elisma@cds-snc.ca');
	  cy.get('input[name="password"]').type('your-password');
	  cy.get('button[type="submit"]').click();
	  cy.contains('Collections').should('be.visible');
	});

	it('should allow creating a new post', () => {
	  cy.visit('/admin');
	  cy.get('input[name="email"]').type('david.elisma@cds-snc.ca');
	  cy.get('input[name="password"]').type('your-password');
	  cy.get('button[type="submit"]').click();
	  cy.contains('New Post').click();
	  cy.get('input[name="title"]').type('My New Post');
	  cy.get('textarea[name="body"]').type('This is the content of my new post.');
	  cy.contains('Save').click();
	  cy.contains('Saved').should('be.visible');
	});
  });