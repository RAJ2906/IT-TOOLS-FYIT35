def login():
    
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.

    if current_user.is_authenticated():

    # if user is logged in we get out of here

        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():

        # Login and validate the user.
        # user should be an instance of your `User` class

	user = models.User.query.filter_by(username=form.login.data).first()
	if user is None or not user.verify_password(form.password.data) or not user.confirmed:
	    flash('Invalid username or password')
	    return redirect(url_for('login'))
        login_user(user)
        flash('Logged in successfully.')
        return redirect(url_for('index'))
    return render_template('login.html', form=form) 
