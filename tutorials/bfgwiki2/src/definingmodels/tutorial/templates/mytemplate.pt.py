registry = dict(version='6.3')
def bind():
	from cPickle import loads as _loads
	_init_stream = _loads('cchameleon.core.generation\ninitialize_stream\np1\n.')
	_lookup_attr = _loads('cchameleon.core.codegen\nlookup_attr\np1\n.')
	_init_scope = _loads('cchameleon.core.utils\necontext\np1\n.')
	_re_amp = _loads("cre\n_compile\np1\n(S'&(?!([A-Za-z]+|#[0-9]+);)'\np2\nI0\ntRp3\n.")
	_init_default = _loads('cchameleon.core.generation\ninitialize_default\np1\n.')
	_lookup_name = _loads('cchameleon.core.codegen\nlookup_name\np1\n.')
	_init_tal = _loads('cchameleon.core.generation\ninitialize_tal\np1\n.')
	def render(econtext):
		macros = econtext.get('macros')
		_slots = econtext.get('_slots')
		target_language = econtext.get('target_language')
		u'_init_stream()'
		(_out, _write) = _init_stream()
		u'_init_tal()'
		(_attributes, repeat) = _init_tal()
		u'_init_default()'
		_default = _init_default()
		u'None'
		default = None
		u'None'
		_domain = None
		u'project'
		_write(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head><title>')
		_tmp1 = econtext['project']
		_tmp = _tmp1
		if (_tmp.__class__ not in (str, unicode) and hasattr(_tmp, '__html__')):
			_write(_tmp.__html__())
		elif _tmp is not None:
			if not (isinstance(_tmp, unicode)):
				_tmp = str(_tmp)
			if '&' in _tmp:
				if ';' in _tmp:
					_tmp = _re_amp.sub('&amp;', _tmp)
				else:
					_tmp = _tmp.replace('&', '&amp;')
			if '<' in _tmp:
				_tmp = _tmp.replace('<', '&lt;')
			if '>' in _tmp:
				_tmp = _tmp.replace('>', '&gt;')
			_write(_tmp)
		_write(u' Application</title>\n<meta name="keywords" content="python web application" />\n<meta name="description" content="repoze.bfg web application" />\n<link')
		default = u'${request.application_url}/static/default.css'
		"join(value('request.application_url'), u'/static/default.css')"
		_tmp1 = ('%s%s' % (_lookup_attr(econtext['request'], 'application_url'), u'/static/default.css'))
		default = None
		if _tmp1 is _default:
			_tmp1 = u'${request.application_url}/static/default.css'
		if (_tmp1 is None or _tmp1 is False):
			pass
		else:
			if not (isinstance(_tmp1, unicode)):
				_tmp1 = str(_tmp1)
			if '&' in _tmp1:
				if ';' in _tmp1:
					_tmp1 = _re_amp.sub('&amp;', _tmp1)
				else:
					_tmp1 = _tmp1.replace('&', '&amp;')
			if '<' in _tmp1:
				_tmp1 = _tmp1.replace('<', '&lt;')
			if '>' in _tmp1:
				_tmp1 = _tmp1.replace('>', '&gt;')
			if '"' in _tmp1:
				_tmp1 = _tmp1.replace('"', '&quot;')
			_write((' href="' + _tmp1) + '"')
		u'project'
		_write(u' rel="stylesheet" type="text/css" />\n</head>\n<body>\n<!-- start header -->\n<div id="logo">\n  <h2><code>')
		_tmp1 = econtext['project']
		_tmp = _tmp1
		if (_tmp.__class__ not in (str, unicode) and hasattr(_tmp, '__html__')):
			_write(_tmp.__html__())
		elif _tmp is not None:
			if not (isinstance(_tmp, unicode)):
				_tmp = str(_tmp)
			if '&' in _tmp:
				if ';' in _tmp:
					_tmp = _re_amp.sub('&amp;', _tmp)
				else:
					_tmp = _tmp.replace('&', '&amp;')
			if '<' in _tmp:
				_tmp = _tmp.replace('<', '&lt;')
			if '>' in _tmp:
				_tmp = _tmp.replace('>', '&gt;')
			_write(_tmp)
		u'project'
		_write(u'</code>, a <code>repoze.bfg</code> application</h2>\n</div>\n<div id="header">\n  <div id="menu">\n  </div>\n</div>\n<!-- end header -->\n<div id="wrapper">\n  <!-- start page -->\n  <div id="page">\n    <!-- start content -->\n    <div id="content">\n      <div class="post">\n\t<h1 class="title">Welcome to <code>')
		_tmp1 = econtext['project']
		_tmp = _tmp1
		if (_tmp.__class__ not in (str, unicode) and hasattr(_tmp, '__html__')):
			_write(_tmp.__html__())
		elif _tmp is not None:
			if not (isinstance(_tmp, unicode)):
				_tmp = str(_tmp)
			if '&' in _tmp:
				if ';' in _tmp:
					_tmp = _re_amp.sub('&amp;', _tmp)
				else:
					_tmp = _tmp.replace('&', '&amp;')
			if '<' in _tmp:
				_tmp = _tmp.replace('<', '&lt;')
			if '>' in _tmp:
				_tmp = _tmp.replace('>', '&gt;')
			_write(_tmp)
		_write(u'</code>, an\n\tapplication generated by the <a href="http://bfg.repoze.org">repoze.bfg</a> web\n\tapplication framework.</h1>\n      </div>\n    </div>\n    <!-- end content -->\n    <!-- start sidebar -->\n    <div id="sidebar">\n      <ul>\n\t<li id="search">\n\t  <h2>Search<br /> <code>repoze.bfg</code> Documentation</h2>\n\t  <form method="get" action="http://bfg.repoze.org/searchresults">\n\t    <fieldset>\n\t      <input type="text" id="q" name="text" value="" />\n\t      <input type="submit" id="x" value="Search" />\n\t    </fieldset>\n\t  </form>\n\t</li>\n\t<li>\n\t  <h2><code>repoze.bfg</code> links</h2>\n\t  <ul>\n\t    <li><a href="http://docs.repoze.org/bfg/#narrative-documentation">Narrative\n\t    Documentation</a>\n            </li>\n\t    <li>\n              <a href="http://docs.repoze.org/bfg/#api-documentation">API\n              Documentation</a>\n            </li>\n\t    <li>\n              <a href="http://docs.repoze.org/bfg/#tutorials">Tutorials</a>\n            </li>\n\t    <li>\n              <a href="http://docs.repoze.org/bfg/#change-history">Change\n              History</a>\n            </li>\n\t    <li>\n              <a href="http://docs.repoze.org/bfg/#sample-applications">Sample\n              Applications</a>\n            </li>\n\t    <li>\n              <a href="http://docs.repoze.org/bfg/#support-and-development">Support\n              and Development</a>\n            </li>\n\t    <li>\n              <a href="irc://irc.freenode.net#repoze">IRC Channel</a>\n            </li>\n\t  </ul>\n\t</li>\n      </ul>\n    </div>\n    <!-- end sidebar -->\n    <div style="clear: both;">&nbsp;</div>\n  </div>\n</div>\n<!-- end page -->\n<!-- start footer -->\n<div id="footer">\n  <p id="legal">( c ) 2008. All Rights Reserved. Template design\n  by <a href="http://www.freecsstemplates.org/">Free CSS\n  Templates</a>.</p>\n</div>\n<!-- end footer -->\n</body>\n</html>')
		return _out.getvalue()
	return render

registry[(None, True, '1488bdb950901f8f258549439ef6661a49aae984')] = bind()
