def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip()

        if not nome or not email:
            flash('O nome e obrigatorio.', 'error')
            return redirect(url_for('cadastro'))

        flash('O email e obrigatorio.', 'success')
        return redirect(url_for('cadastro'))

    return render_template('cadastro.html')