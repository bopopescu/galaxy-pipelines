# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1382377811.626669
_template_filename='templates/user/dbkeys.mako'
_template_uri='user/dbkeys.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['body', 'title', 'center_panel', 'stylesheets', 'init', 'javascripts']


# SOURCE LINE 1

def inherit(context):
    if context.get('use_panels'):
        return '/webapps/galaxy/base_panels.mako'
    else:
        return '/base.mako'


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n')
        # SOURCE LINE 8
        __M_writer(u'\n\n')
        # SOURCE LINE 18
        __M_writer(u'\n\n')
        # SOURCE LINE 20
        __M_writer(u'\n\n')
        # SOURCE LINE 49
        __M_writer(u'\n\n')
        # SOURCE LINE 108
        __M_writer(u'\n\n')
        # SOURCE LINE 112
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        installed_len_files = context.get('installed_len_files', UNDEFINED)
        lines_skipped = context.get('lines_skipped', UNDEFINED)
        dbkeys = context.get('dbkeys', UNDEFINED)
        fasta_hdas = context.get('fasta_hdas', UNDEFINED)
        message = context.get('message', UNDEFINED)
        use_panels = context.get('use_panels', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 114
        __M_writer(u'\n')
        # SOURCE LINE 115
        if message:
            # SOURCE LINE 116
            __M_writer(u'        <div class="errormessagelarge">')
            __M_writer(unicode(message))
            __M_writer(u'</div>\n')
            # SOURCE LINE 117
        elif lines_skipped > 0:
            # SOURCE LINE 118
            __M_writer(u'        <div class="warningmessagelarge">Skipped ')
            __M_writer(unicode(lines_skipped))
            __M_writer(u' lines that could not be parsed. (Line was either blank or not 2-column, with 2nd column being an integer)</div>\n')
            pass
        # SOURCE LINE 120
        __M_writer(u'\n    <h3>Current Custom Builds:</h3>\n\n')
        # SOURCE LINE 123
        if dbkeys:
            # SOURCE LINE 124
            __M_writer(u'        <table id="custom_dbkeys" class="colored" cellspacing="0" cellpadding="0">\n            <tr class="header">\n                <th>Name</th>\n                <th>Key</th>\n                <th>Number of chroms/contigs</th>\n                <th></th>\n            </tr>\n')
            # SOURCE LINE 131
            for key, dct in dbkeys.iteritems():
                # SOURCE LINE 132
                __M_writer(u'            <tr>\n                <td>')
                # SOURCE LINE 133
                __M_writer(filters.html_escape(unicode(dct['name'] )))
                __M_writer(u'</td>\n                <td>')
                # SOURCE LINE 134
                __M_writer(filters.html_escape(unicode(key )))
                __M_writer(u'</td>\n                <td>\n')
                # SOURCE LINE 145
                if 'count' in dct:
                    # SOURCE LINE 146
                    __M_writer(u'                        ')
                    __M_writer(unicode(dct['count']))
                    __M_writer(u'\n')
                    # SOURCE LINE 147
                else:
                    # SOURCE LINE 148
                    __M_writer(u'                        Processing\n')
                    pass
                # SOURCE LINE 150
                __M_writer(u'                </td>\n                <td><form action="dbkeys" method="post"><input type="hidden" name="key" value="')
                # SOURCE LINE 151
                __M_writer(unicode(key))
                __M_writer(u'" /><input type="submit" name="delete" value="Delete" /></form></td>\n            </tr>\n')
                pass
            # SOURCE LINE 154
            __M_writer(u'        </table>\n')
            # SOURCE LINE 155
        else:
            # SOURCE LINE 156
            __M_writer(u'        <p>You currently have no custom builds.</p>\n')
            pass
        # SOURCE LINE 158
        __M_writer(u'    \n    <p>\n        <a id="show_installed_builds" href="javascript:void(0);">Show loaded, system-installed builds</a>\n        <blockquote id="installed_builds">')
        # SOURCE LINE 161
        __M_writer(unicode(installed_len_files))
        __M_writer(u'</blockquote>\n    </p>\n    \n    <hr />\n    <h3>Add a Custom Build</h3>\n    <form action="dbkeys" method="post" enctype="multipart/form-data">\n')
        # SOURCE LINE 168
        if use_panels:
            # SOURCE LINE 169
            __M_writer(u'            <input type="hidden" name="use_panels" value="True">\n')
            pass
        # SOURCE LINE 172
        __M_writer(u'        <div class="toolForm" style="float: left;">\n            <div class="toolFormTitle">New Build</div>\n            <div class="toolFormBody">\n                <div class="form-row">\n                    <label for="name">Name (eg: Hamster):</label>\n                    <input type="text" id="name" name="name" />\n                </div>\n                <div class="form-row">\n                    <label for="key">Key (eg: hamster_v1):</label>\n                    <input type="text" id="key" name="key" />\n                </div>\n                <div class="form-row build_definition">\n                    <label>Definition:</label>\n                    <div class="def_tab">\n                        <a id="fasta" href="javascript:void(0)">FASTA</a>\n                    </div>\n                    <div class="def_tab">\n                        <a id="len_file" href="javascript:void(0)">Len File</a>\n                    </div>\n                    <div class="def_tab">\n                        <a id="len_entry" href="javascript:void(0)">Len Entry</a>\n                    </div>\n                    <div style="clear: both; padding-bottom: 0.5em"></div>\n                    <select id="fasta_input" name="dataset_id">\n')
        # SOURCE LINE 196
        for dataset in fasta_hdas:
            # SOURCE LINE 197
            __M_writer(u'                        <option value="')
            __M_writer(unicode(trans.security.encode_id( dataset.id )))
            __M_writer(u'">')
            __M_writer(unicode(dataset.hid))
            __M_writer(u': ')
            __M_writer(unicode(dataset.name))
            __M_writer(u'</option>\n')
            pass
        # SOURCE LINE 199
        __M_writer(u'                    </select>\n                    <input type="file" id="len_file_input" name="len_file" /></input>\n                    <textarea id="len_entry_input" name="len_text" cols="30" rows="8"></textarea>\n                </div>            \n                <div class="form-row"><input id="submit" type="submit" name="add" value="Submit"/></div>\n            </div>\n        </div>\n    </form>\n    <div class="infomessagesmall" style="float: left; margin-left: 10px; width: 40%;">\n        <div class="fasta_help">\n            <h3>FASTA format</h3>\n            <p>\n                This is a multi-fasta file from your current history that provides the genome \n                sequences for each chromosome/contig in your build.\n            </p>\n            \n            <p>\n                Here is a snippet from an example multi-fasta file:\n                <pre>\n    >chr1\n    ATTATATATAAGACCACAGAGAGAATATTTTGCCCGG...\n    >chr2\n    GGCGGCCGCGGCGATATAGAACTACTCATTATATATA...\n    ...\n                </pre>\n            </p>\n        </div>\n        <div class="len_file_help len_entry_help">\n            <h3>Length Format</h3>\n            <p>\n                The length format is two-column, separated by whitespace, of the form:\n                <pre>chrom/contig   length of chrom/contig</pre>\n            </p>\n            <p>\n                For example, the first few entries of <em>mm9.len</em> are as follows:\n                <pre>\n    chr1    197195432\n    chr2    181748087\n    chr3    159599783\n    chr4    155630120\n    chr5    152537259\n                </pre>\n            </p>\n        \n            <p>Trackster uses this information to populate the select box for chrom/contig, and\n            to set the maximum basepair of the track browser. You may either upload a .len file\n            of this format (Len File option), or directly enter the information into the box \n            (Len Entry option).</p>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 20
        __M_writer(u'Custom Database Builds')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 110
        __M_writer(u'\n    ')
        # SOURCE LINE 111
        __M_writer(unicode(self.body()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n    ')
        # SOURCE LINE 23
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    <style type="text/css">\n        #custom_dbkeys * {\n            min-width: 100px;\n            vertical-align: text-top;\n        }\n        pre {\n            padding: 0;\n            margin: 0;\n        }\n')
        # SOURCE LINE 34
        if context.get('use_panels'):
            # SOURCE LINE 35
            __M_writer(u'        div#center {\n            padding: 10px;\n        }\n')
            pass
        # SOURCE LINE 39
        __M_writer(u'        div.def_tab {\n            float: left;\n            padding: 0.2em 0.5em;\n            background-color: white;\n        }\n        div.def_tab.active {\n            background-color: #CCF;\n            border: solid 1px #66A;\n        }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 10
        __M_writer(u'\n')
        # SOURCE LINE 11

        self.has_left_panel=False
        self.has_right_panel=False
        self.message_box_visible=False
        self.active_view="user"
        self.overlay_visible=False
        
        
        # SOURCE LINE 17
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        fasta_hdas = context.get('fasta_hdas', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 51
        __M_writer(u'\n   ')
        # SOURCE LINE 52
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n   \n    <script type="text/javascript">\n\n    $(function() {\n        $(".db_hide").each(function() {\n            var pre = $(this);\n            pre.hide();\n            pre.siblings("span").wrap( "<a href=\'javascript:void(0);\'></a>" ).click( function() {\n                pre.toggle();\n            });     \n        });\n        $("#installed_builds").hide();\n        $("#show_installed_builds").click(function() {\n            $("#installed_builds").show();\n        });\n        \n        // Set up behavior for build definition tab controls.\n        $("div.def_tab > a").each(function() {\n            $(this).click(function() {\n                var tab_id = $(this).attr("id");\n\n                // Hide all build inputs, help.\n                $("div.build_definition").children(":input").hide();\n                $(".infomessagesmall > div").hide();\n                \n                // Show input item, help corresponding to tab id.\n                $("#" + tab_id + "_input").show();\n                $("." + tab_id + "_help").show();\n                \n                // Update tabs.\n                $("div.def_tab").removeClass("active");\n                $(this).parent().addClass("active");\n            });\n        });\n        \n')
        # SOURCE LINE 89
        __M_writer(u'        // Set starting tab.\n')
        # SOURCE LINE 90
        if fasta_hdas.first():
            # SOURCE LINE 91
            __M_writer(u'            $("#fasta").click();\n')
            # SOURCE LINE 92
        else:
            # SOURCE LINE 93
            __M_writer(u'            $("#len_file").click();\n')
            pass
        # SOURCE LINE 95
        __M_writer(u'        \n        // Before submit, remove inputs not associated with the active tab.\n        $("#submit").click(function() {\n            var id = $(this).parents("form").find(".active > a").attr("id");\n            $("div.build_definition").children(":input").each(function() {\n                if ( $(this).attr("id") !== (id + "_input")  ) {\n                    $(this).remove();\n                }\n            });\n        });\n    });\n\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


