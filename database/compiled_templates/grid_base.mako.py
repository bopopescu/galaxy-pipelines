# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1382462618.088629
_template_filename=u'templates/grid_base.mako'
_template_uri=u'/grid_base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['body', 'grid_title', 'render_grid_header', 'title', 'center_panel', 'render_grid_table_body_contents', 'stylesheets', 'grid_javascripts', 'init', 'render_grid_table', 'grid_body', 'make_grid', 'render_grid_table_footer_contents', 'javascripts']


# SOURCE LINE 1

from galaxy.web.framework.helpers.grids import TextColumn
import galaxy.util
def inherit(context):
    if context.get('use_panels'):
        if context.get('webapp'):
            webapp = context.get('webapp')
        else:
            webapp = 'galaxy'
        return '/webapps/%s/base_panels.mako' % webapp
    else:
        return '/base.mako'


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 15
    ns = runtime.TemplateNamespace('__anon_0x7fae9c32a990', context._clean_inheritance_tokens(), templateuri=u'/display_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fae9c32a990')] = ns

    # SOURCE LINE 358
    ns = runtime.TemplateNamespace('__anon_0x7faecc5f5310', context._clean_inheritance_tokens(), templateuri=u'/display_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7faecc5f5310')] = ns

    # SOURCE LINE 16
    ns = runtime.TemplateNamespace('__anon_0x7fae9c32a590', context._clean_inheritance_tokens(), templateuri=u'/refresh_frames.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fae9c32a590')] = ns

    # SOURCE LINE 132
    ns = runtime.TemplateNamespace('__anon_0x7fae9421f790', context._clean_inheritance_tokens(), templateuri=u'./grid_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fae9421f790')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fae9c32a990')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x7faecc5f5310')._populate(_import_ns, [u'get_class_plural'])
        _mako_get_namespace(context, '__anon_0x7fae9c32a590')._populate(_import_ns, [u'handle_refresh_frames'])
        _mako_get_namespace(context, '__anon_0x7fae9421f790')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer(u'\n')
        # SOURCE LINE 14
        __M_writer(u'\n')
        # SOURCE LINE 15
        __M_writer(u'\n')
        # SOURCE LINE 16
        __M_writer(u'\n\n')
        # SOURCE LINE 26
        __M_writer(u'\n\n')
        # SOURCE LINE 31
        __M_writer(u'\n')
        # SOURCE LINE 34
        __M_writer(u'\n\n')
        # SOURCE LINE 39
        __M_writer(u'\n\n')
        # SOURCE LINE 46
        __M_writer(u'\n\n')
        # SOURCE LINE 48
        __M_writer(u'\n\n')
        # SOURCE LINE 53
        __M_writer(u'\n\n')
        # SOURCE LINE 113
        __M_writer(u'\n\n')
        # SOURCE LINE 126
        __M_writer(u'\n\n')
        # SOURCE LINE 131
        __M_writer(u'\n')
        # SOURCE LINE 132
        __M_writer(u'\n\n')
        # SOURCE LINE 150
        __M_writer(u'\n\n')
        # SOURCE LINE 154
        __M_writer(u'\n\n')
        # SOURCE LINE 182
        __M_writer(u'\n\n')
        # SOURCE LINE 250
        __M_writer(u'\n\n')
        # SOURCE LINE 353
        __M_writer(u'\n\n')
        # SOURCE LINE 457
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fae9c32a990')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x7faecc5f5310')._populate(_import_ns, [u'get_class_plural'])
        _mako_get_namespace(context, '__anon_0x7fae9c32a590')._populate(_import_ns, [u'handle_refresh_frames'])
        _mako_get_namespace(context, '__anon_0x7fae9421f790')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        grid = _import_ns.get('grid', context.get('grid', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 37
        __M_writer(u'\n    ')
        # SOURCE LINE 38
        __M_writer(unicode(self.grid_body( grid )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_grid_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fae9c32a990')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x7faecc5f5310')._populate(_import_ns, [u'get_class_plural'])
        _mako_get_namespace(context, '__anon_0x7fae9c32a590')._populate(_import_ns, [u'handle_refresh_frames'])
        _mako_get_namespace(context, '__anon_0x7fae9421f790')._populate(_import_ns, [u'*'])
        grid = _import_ns.get('grid', context.get('grid', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 152
        __M_writer(u'\n    <h2>')
        # SOURCE LINE 153
        __M_writer(unicode(grid.title))
        __M_writer(u'</h2>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_grid_header(context,grid,render_title=True):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fae9c32a990')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x7faecc5f5310')._populate(_import_ns, [u'get_class_plural'])
        _mako_get_namespace(context, '__anon_0x7fae9c32a590')._populate(_import_ns, [u'handle_refresh_frames'])
        _mako_get_namespace(context, '__anon_0x7fae9421f790')._populate(_import_ns, [u'*'])
        url = _import_ns.get('url', context.get('url', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        render_grid_filters = _import_ns.get('render_grid_filters', context.get('render_grid_filters', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 157
        __M_writer(u'\n    <div class="grid-header">\n')
        # SOURCE LINE 159
        if render_title:
            # SOURCE LINE 160
            __M_writer(u'            ')
            __M_writer(unicode(self.grid_title()))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 162
        __M_writer(u'    \n')
        # SOURCE LINE 163
        if grid.global_actions:
            # SOURCE LINE 164
            __M_writer(u'            <ul class="manage-table-actions">\n')
            # SOURCE LINE 165
            if len( grid.global_actions ) < 3:
                # SOURCE LINE 166
                for action in grid.global_actions:
                    # SOURCE LINE 167
                    __M_writer(u'                        <li><a class="action-button" href="')
                    __M_writer(unicode(url( **action.url_args )))
                    __M_writer(u'">')
                    __M_writer(unicode(action.label))
                    __M_writer(u'</a></li>\n')
                    pass
                # SOURCE LINE 169
            else:
                # SOURCE LINE 170
                __M_writer(u'                    <li><a class="action-button" id="action-8675309-popup" class="menubutton">Actions</a></li>\n                    <div popupmenu="action-8675309-popup">\n')
                # SOURCE LINE 172
                for action in grid.global_actions:
                    # SOURCE LINE 173
                    __M_writer(u'                            <a class="action-button" href="')
                    __M_writer(unicode(url( **action.url_args )))
                    __M_writer(u'">')
                    __M_writer(unicode(action.label))
                    __M_writer(u'</a>\n')
                    pass
                # SOURCE LINE 175
                __M_writer(u'                    </div>\n')
                pass
            # SOURCE LINE 177
            __M_writer(u'            </ul>\n')
            pass
        # SOURCE LINE 179
        __M_writer(u'    \n        ')
        # SOURCE LINE 180
        __M_writer(unicode(render_grid_filters( grid )))
        __M_writer(u'\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fae9c32a990')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x7faecc5f5310')._populate(_import_ns, [u'get_class_plural'])
        _mako_get_namespace(context, '__anon_0x7fae9c32a590')._populate(_import_ns, [u'handle_refresh_frames'])
        _mako_get_namespace(context, '__anon_0x7fae9421f790')._populate(_import_ns, [u'*'])
        grid = _import_ns.get('grid', context.get('grid', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 48
        __M_writer(unicode(grid.title))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fae9c32a990')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x7faecc5f5310')._populate(_import_ns, [u'get_class_plural'])
        _mako_get_namespace(context, '__anon_0x7fae9c32a590')._populate(_import_ns, [u'handle_refresh_frames'])
        _mako_get_namespace(context, '__anon_0x7fae9421f790')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        grid = _import_ns.get('grid', context.get('grid', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer(u'\n    ')
        # SOURCE LINE 33
        __M_writer(unicode(self.grid_body( grid )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_grid_table_body_contents(context,grid,show_item_checkboxes=False):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fae9c32a990')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x7faecc5f5310')._populate(_import_ns, [u'get_class_plural'])
        _mako_get_namespace(context, '__anon_0x7fae9c32a590')._populate(_import_ns, [u'handle_refresh_frames'])
        _mako_get_namespace(context, '__anon_0x7fae9421f790')._populate(_import_ns, [u'*'])
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        str = _import_ns.get('str', context.get('str', UNDEFINED))
        url = _import_ns.get('url', context.get('url', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        current_item = _import_ns.get('current_item', context.get('current_item', UNDEFINED))
        unicode = _import_ns.get('unicode', context.get('unicode', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        query = _import_ns.get('query', context.get('query', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 253
        __M_writer(u'\n        ')
        # SOURCE LINE 254
        num_rows_rendered = 0 
        
        __M_writer(u'\n')
        # SOURCE LINE 255
        if query.count() == 0:
            # SOURCE LINE 257
            __M_writer(u'            <tr><td colspan="100"><em>No Items</em></td></tr>\n            ')
            # SOURCE LINE 258
            num_rows_rendered = 1 
            
            __M_writer(u'\n')
            pass
        # SOURCE LINE 260
        for i, item in enumerate( query ):
            # SOURCE LINE 261
            __M_writer(u'            ')
            encoded_id = trans.security.encode_id( item.id ) 
            
            __M_writer(u'\n            <tr ')
            # SOURCE LINE 263
            if current_item == item:
                # SOURCE LINE 264
                __M_writer(u'                class="current" ')
                pass
            # SOURCE LINE 266
            __M_writer(u'            > \n')
            # SOURCE LINE 268
            if show_item_checkboxes:
                # SOURCE LINE 269
                __M_writer(u'                    <td style="width: 1.5em;">\n                        <input type="checkbox" name="id" value="')
                # SOURCE LINE 270
                __M_writer(unicode(encoded_id))
                __M_writer(u'" id="')
                __M_writer(unicode(encoded_id))
                __M_writer(u'" class="grid-row-select-checkbox" />\n                    </td>\n')
                pass
            # SOURCE LINE 274
            for column in grid.columns:
                # SOURCE LINE 275
                if column.visible:
                    # SOURCE LINE 276
                    __M_writer(u'                        ')

                            # Nowrap
                    nowrap = ""
                    if column.nowrap:
                      nowrap = 'style="white-space:nowrap;"'
                    # Link
                    link = column.get_link( trans, grid, item )
                    if link:
                        href = url( **link )
                    else:
                        href = None
                    # Value (coerced to list so we can loop)
                    value = column.get_value( trans, grid, item )
                    if column.ncells == 1:
                        value = [ value ]
                                            
                    
                    # SOURCE LINE 291
                    __M_writer(u'\n')
                    # SOURCE LINE 292
                    for cellnum, v in enumerate( value ):
                        # SOURCE LINE 293
                        __M_writer(u'                            ')

                        id = ""
                        # Handle non-ascii chars.
                        if isinstance(v, str):
                            v = unicode(v, 'utf-8')
                        # Attach popup menu?
                        if column.attach_popup and cellnum == 0:
                            id = 'grid-%d-popup' % i
                        # Determine appropriate class
                        cls = ""
                        if column.attach_popup:
                            cls = "menubutton"
                            if href:
                                cls += " split"
                        
                                                    
                        
                        # SOURCE LINE 308
                        __M_writer(u'\n                            <td ')
                        # SOURCE LINE 309
                        __M_writer(unicode(nowrap))
                        __M_writer(u'>\n')
                        # SOURCE LINE 310
                        if href:
                            # SOURCE LINE 311
                            if len(grid.operations) != 0:
                                # SOURCE LINE 312
                                __M_writer(u'                                <div id="')
                                __M_writer(unicode(id))
                                __M_writer(u'" class="')
                                __M_writer(unicode(cls))
                                __M_writer(u'" style="float: left;">\n')
                                pass
                            # SOURCE LINE 314
                            __M_writer(u'                                    <a class="label" href="')
                            __M_writer(unicode(href))
                            __M_writer(u'">')
                            __M_writer(unicode(v))
                            __M_writer(u'</a>\n')
                            # SOURCE LINE 315
                            if len(grid.operations) != 0:
                                # SOURCE LINE 316
                                __M_writer(u'                                </div>\n')
                                pass
                            # SOURCE LINE 318
                        else:
                            # SOURCE LINE 319
                            __M_writer(u'                                <div id="')
                            __M_writer(unicode(id))
                            __M_writer(u'" class="')
                            __M_writer(unicode(cls))
                            __M_writer(u'"><label id="')
                            __M_writer(unicode(column.label_id_prefix))
                            __M_writer(unicode(encoded_id))
                            __M_writer(u'" for="')
                            __M_writer(unicode(encoded_id))
                            __M_writer(u'">')
                            __M_writer(unicode(v))
                            __M_writer(u'</label></div>\n')
                            pass
                        # SOURCE LINE 321
                        __M_writer(u'                            </td>\n')
                        pass
                    pass
                pass
            # SOURCE LINE 326
            __M_writer(u'                <td>\n                    <div popupmenu="grid-')
            # SOURCE LINE 327
            __M_writer(unicode(i))
            __M_writer(u'-popup">\n')
            # SOURCE LINE 328
            for operation in grid.operations:
                # SOURCE LINE 329
                if operation.allowed( item ) and operation.allow_popup:
                    # SOURCE LINE 330
                    __M_writer(u'                                ')

                    target = ""
                    if operation.target:
                        target = "target='" + operation.target + "'"
                    
                    
                    # SOURCE LINE 334
                    __M_writer(u'\n')
                    # SOURCE LINE 335
                    if operation.confirm:
                        # SOURCE LINE 336
                        __M_writer(u'                                    <a class="action-button" ')
                        __M_writer(unicode(target))
                        __M_writer(u' confirm="')
                        __M_writer(unicode(operation.confirm))
                        __M_writer(u'" href="')
                        __M_writer(unicode( url( **operation.get_url_args( item ) ) ))
                        __M_writer(u'">')
                        __M_writer(unicode(operation.label))
                        __M_writer(u'</a>\n')
                        # SOURCE LINE 337
                    else:
                        # SOURCE LINE 338
                        __M_writer(u'                                    <a class="action-button" ')
                        __M_writer(unicode(target))
                        __M_writer(u' href="')
                        __M_writer(unicode( url( **operation.get_url_args( item ) ) ))
                        __M_writer(u'">')
                        __M_writer(unicode(operation.label))
                        __M_writer(u'</a>\n')
                        pass
                    pass
                pass
            # SOURCE LINE 342
            __M_writer(u'                    </div>\n                </td>\n            </tr>\n            ')
            # SOURCE LINE 345
            num_rows_rendered += 1 
            
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fae9c32a990')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x7faecc5f5310')._populate(_import_ns, [u'get_class_plural'])
        _mako_get_namespace(context, '__anon_0x7fae9c32a590')._populate(_import_ns, [u'handle_refresh_frames'])
        _mako_get_namespace(context, '__anon_0x7fae9421f790')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 115
        __M_writer(u'\n    ')
        # SOURCE LINE 116
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 117
        __M_writer(unicode(h.css( "autocomplete_tagging", "jquery.rating" )))
        __M_writer(u'\n    <style>\n')
        # SOURCE LINE 120
        if context.get('use_panels'):
            # SOURCE LINE 121
            __M_writer(u'        div#center {\n            padding: 10px;\n        }\n')
            pass
        # SOURCE LINE 125
        __M_writer(u'    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_grid_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fae9c32a990')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x7faecc5f5310')._populate(_import_ns, [u'get_class_plural'])
        _mako_get_namespace(context, '__anon_0x7fae9c32a590')._populate(_import_ns, [u'handle_refresh_frames'])
        _mako_get_namespace(context, '__anon_0x7fae9421f790')._populate(_import_ns, [u'*'])
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        num_pages = _import_ns.get('num_pages', context.get('num_pages', UNDEFINED))
        cur_filter_dict = _import_ns.get('cur_filter_dict', context.get('cur_filter_dict', UNDEFINED))
        sort_key = _import_ns.get('sort_key', context.get('sort_key', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        handle_refresh_frames = _import_ns.get('handle_refresh_frames', context.get('handle_refresh_frames', UNDEFINED))
        cur_page_num = _import_ns.get('cur_page_num', context.get('cur_page_num', UNDEFINED))
        grid = _import_ns.get('grid', context.get('grid', UNDEFINED))
        url = _import_ns.get('url', context.get('url', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 55
        __M_writer(u'\n    ')
        # SOURCE LINE 56
        __M_writer(unicode(h.js("libs/jquery/jquery.autocomplete", "galaxy.autocom_tagging", "libs/jquery/jquery.rating", "galaxy.grids" )))
        __M_writer(u'\n    ')
        # SOURCE LINE 57
        __M_writer(unicode(handle_refresh_frames()))
        __M_writer(u'\n    \n    <script type="text/javascript">\n        \n        // Needed URLs for grid history searching.\n        var history_tag_autocomplete_url = "')
        # SOURCE LINE 62
        __M_writer(unicode(url( controller='tag', action='tag_autocomplete_data', item_class='History' )))
        __M_writer(u'",\n            history_name_autocomplete_url = "')
        # SOURCE LINE 63
        __M_writer(unicode(url( controller='history', action='name_autocomplete_data' )))
        __M_writer(u'";\n\n        //\n        // Create grid object.\n        //\n\n        // Operations that are async (AJAX) compatible.\n        var async_ops = [];\n')
        # SOURCE LINE 71
        for operation in [op for op in grid.operations if op.async_compatible]:
            # SOURCE LINE 72
            __M_writer(u"            async_ops.push('")
            __M_writer(unicode(operation.label.lower()))
            __M_writer(u"');\n")
            pass
        # SOURCE LINE 74
        __M_writer(u'\n        // Filter values for categorical filters.\n        var categorical_filters = {};\n')
        # SOURCE LINE 77
        for column in grid.columns:
            # SOURCE LINE 78
            if column.filterable is not None and not isinstance( column, TextColumn ):
                # SOURCE LINE 79
                __M_writer(u'                var ')
                __M_writer(unicode(column.key))
                __M_writer(u'_filters = ')
                __M_writer(unicode( h.to_json_string( dict([ (filter.label, filter.args) for filter in column.get_accepted_filters() ]) ) ))
                __M_writer(u";\n                categorical_filters['")
                # SOURCE LINE 80
                __M_writer(unicode(column.key))
                __M_writer(u"'] = ")
                __M_writer(unicode(column.key))
                __M_writer(u'_filters;\n')
                pass
            pass
        # SOURCE LINE 83
        __M_writer(u"\n        /** Returns true if string denotes true. */\n        var is_true = function(s) { return _.indexOf(['True', 'true', 't'], s) !== -1; };\n\n\n        // Create grid.\n        var grid = new Grid({\n            url_base: '")
        # SOURCE LINE 90
        __M_writer(unicode(trans.request.path_url))
        __M_writer(u"',\n            async: is_true('")
        # SOURCE LINE 91
        __M_writer(unicode(grid.use_async))
        __M_writer(u"'),\n            async_ops: async_ops,\n            categorical_filters: categorical_filters,\n            filters: ")
        # SOURCE LINE 94
        __M_writer(unicode(h.to_json_string( cur_filter_dict )))
        __M_writer(u",\n            sort_key: '")
        # SOURCE LINE 95
        __M_writer(unicode(sort_key))
        __M_writer(u"',\n            show_item_checkboxes: is_true('")
        # SOURCE LINE 96
        __M_writer(unicode(context.get('show_item_checkboxes', False)))
        __M_writer(u"'),\n            cur_page: ")
        # SOURCE LINE 97
        __M_writer(unicode(cur_page_num))
        __M_writer(u',\n            num_pages: ')
        # SOURCE LINE 98
        __M_writer(unicode(num_pages))
        __M_writer(u'\n        });\n\n        // Initialize grid objects on load.\n        // FIXME: use a grid view object eventually.\n        $(document).ready(function() {\n            init_grid_elements();\n            init_grid_controls();\n            // Initialize text filters to select text on click and use normal font when user is typing.\n            $(\'input[type=text]\').each(function() {\n                $(this).click(function() { $(this).select(); } )\n                       .keyup(function () { $(this).css("font-style", "normal"); });\n            });\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fae9c32a990')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x7faecc5f5310')._populate(_import_ns, [u'get_class_plural'])
        _mako_get_namespace(context, '__anon_0x7fae9c32a590')._populate(_import_ns, [u'handle_refresh_frames'])
        _mako_get_namespace(context, '__anon_0x7fae9421f790')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 18
        __M_writer(u'\n')
        # SOURCE LINE 19

        self.has_left_panel=False
        self.has_right_panel=False
        self.message_box_visible=False
        self.active_view="user"
        self.overlay_visible=False
        
        
        # SOURCE LINE 25
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_grid_table(context,grid,show_item_checkboxes=False):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fae9c32a990')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x7faecc5f5310')._populate(_import_ns, [u'get_class_plural'])
        _mako_get_namespace(context, '__anon_0x7fae9c32a590')._populate(_import_ns, [u'handle_refresh_frames'])
        _mako_get_namespace(context, '__anon_0x7fae9421f790')._populate(_import_ns, [u'*'])
        sort_key = _import_ns.get('sort_key', context.get('sort_key', UNDEFINED))
        url = _import_ns.get('url', context.get('url', UNDEFINED))
        def render_grid_table_footer_contents(grid,show_item_checkboxes=False):
            return render_render_grid_table_footer_contents(context,grid,show_item_checkboxes)
        def render_grid_table_body_contents(grid,show_item_checkboxes=False):
            return render_render_grid_table_body_contents(context,grid,show_item_checkboxes)
        query = _import_ns.get('query', context.get('query', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 185
        __M_writer(u'\n    ')
        # SOURCE LINE 186

        # Set flag to indicate whether grid has operations that operate on multiple items.
        multiple_item_ops_exist = False
        for operation in grid.operations:
            if operation.allow_multiple:
                multiple_item_ops_exist = True
                
        # Show checkboxes if flag is set or if multiple item ops exist.
        if show_item_checkboxes or multiple_item_ops_exist:
            show_item_checkboxes = True
            
        
        # SOURCE LINE 196
        __M_writer(u'\n    <form action="')
        # SOURCE LINE 197
        __M_writer(unicode(url()))
        __M_writer(u'" method="post" onsubmit="return false;">\n        <table id="grid-table" class="grid">\n            <thead id="grid-table-header">\n                <tr>\n')
        # SOURCE LINE 201
        if show_item_checkboxes:
            # SOURCE LINE 202
            __M_writer(u'                        <th>\n')
            # SOURCE LINE 203
            if query.count() > 0:
                # SOURCE LINE 204
                __M_writer(u'                                <input type="checkbox" id="check_all" name=select_all_checkbox value="true" onclick=\'check_all_items(1);\'><input type="hidden" name=select_all_checkbox value="true">\n')
                pass
            # SOURCE LINE 206
            __M_writer(u'                        </th>\n')
            pass
        # SOURCE LINE 208
        for column in grid.columns:
            # SOURCE LINE 209
            if column.visible:
                # SOURCE LINE 210
                __M_writer(u'                            ')

                href = ""
                extra = ""
                if column.sortable:
                    if sort_key.endswith(column.key):
                        if not sort_key.startswith("-"):
                            href = url( sort=( "-" + column.key ) )
                            extra = "&darr;"
                        else:
                            href = url( sort=( column.key ) )
                            extra = "&uarr;"
                    else:
                        href = url( sort=column.key )
                                            
                
                # SOURCE LINE 223
                __M_writer(u'\n                            <th')
                # SOURCE LINE 225
                __M_writer(u'                            id="')
                __M_writer(unicode(column.key))
                __M_writer(u'-header"\n')
                # SOURCE LINE 226
                if column.ncells > 1:
                    # SOURCE LINE 227
                    __M_writer(u'                                colspan="')
                    __M_writer(unicode(column.ncells))
                    __M_writer(u'"\n')
                    pass
                # SOURCE LINE 229
                __M_writer(u'                            >\n')
                # SOURCE LINE 230
                if href:
                    # SOURCE LINE 231
                    __M_writer(u'                                    <a href="')
                    __M_writer(unicode(href))
                    __M_writer(u'" class="sort-link" sort_key="')
                    __M_writer(unicode(column.key))
                    __M_writer(u'">')
                    __M_writer(unicode(column.label))
                    __M_writer(u'</a>\n')
                    # SOURCE LINE 232
                else:
                    # SOURCE LINE 233
                    __M_writer(u'                                    ')
                    __M_writer(unicode(column.label))
                    __M_writer(u'\n')
                    pass
                # SOURCE LINE 235
                __M_writer(u'                                <span class="sort-arrow">')
                __M_writer(unicode(extra))
                __M_writer(u'</span>\n                            </th>\n')
                pass
            pass
        # SOURCE LINE 239
        __M_writer(u'                    <th></th>\n                </tr>\n            </thead>\n            <tbody id="grid-table-body">\n                ')
        # SOURCE LINE 243
        __M_writer(unicode(render_grid_table_body_contents( grid, show_item_checkboxes )))
        __M_writer(u'\n            </tbody>\n            <tfoot id="grid-table-footer">\n                ')
        # SOURCE LINE 246
        __M_writer(unicode(render_grid_table_footer_contents( grid, show_item_checkboxes )))
        __M_writer(u'\n            </tfoot>\n        </table>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_grid_body(context,grid):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fae9c32a990')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x7faecc5f5310')._populate(_import_ns, [u'get_class_plural'])
        _mako_get_namespace(context, '__anon_0x7fae9c32a590')._populate(_import_ns, [u'handle_refresh_frames'])
        _mako_get_namespace(context, '__anon_0x7fae9421f790')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 44
        __M_writer(u'\n    ')
        # SOURCE LINE 45
        __M_writer(unicode(self.make_grid( grid )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_make_grid(context,grid):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fae9c32a990')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x7faecc5f5310')._populate(_import_ns, [u'get_class_plural'])
        _mako_get_namespace(context, '__anon_0x7fae9c32a590')._populate(_import_ns, [u'handle_refresh_frames'])
        _mako_get_namespace(context, '__anon_0x7fae9421f790')._populate(_import_ns, [u'*'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        show_item_checkboxes = _import_ns.get('show_item_checkboxes', context.get('show_item_checkboxes', UNDEFINED))
        render_message = _import_ns.get('render_message', context.get('render_message', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 134
        __M_writer(u'\n    <div class="loading-elt-overlay"></div>\n    <table>\n        <tr>\n            <td width="75%">')
        # SOURCE LINE 138
        __M_writer(unicode(self.render_grid_header( grid )))
        __M_writer(u'</td>\n            <td></td>\n            <td></td>\n        </tr>\n        <tr>\n            <td width="100%" id="grid-message" valign="top">')
        # SOURCE LINE 143
        __M_writer(unicode(render_message( message, status )))
        __M_writer(u'</td>\n            <td></td>\n            <td></td>\n        </tr>\n    </table>\n\n    ')
        # SOURCE LINE 149
        __M_writer(unicode(self.render_grid_table( grid, show_item_checkboxes )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_grid_table_footer_contents(context,grid,show_item_checkboxes=False):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fae9c32a990')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x7faecc5f5310')._populate(_import_ns, [u'get_class_plural'])
        _mako_get_namespace(context, '__anon_0x7fae9c32a590')._populate(_import_ns, [u'handle_refresh_frames'])
        _mako_get_namespace(context, '__anon_0x7fae9421f790')._populate(_import_ns, [u'*'])
        num_pages = _import_ns.get('num_pages', context.get('num_pages', UNDEFINED))
        url = _import_ns.get('url', context.get('url', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        cur_page_num = _import_ns.get('cur_page_num', context.get('cur_page_num', UNDEFINED))
        range = _import_ns.get('range', context.get('range', UNDEFINED))
        get_class_plural = _import_ns.get('get_class_plural', context.get('get_class_plural', UNDEFINED))
        num_page_links = _import_ns.get('num_page_links', context.get('num_page_links', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 356
        __M_writer(u'\n')
        # SOURCE LINE 358
        __M_writer(u'    ')
        __M_writer(u'\n    ')
        # SOURCE LINE 359
        items_plural = get_class_plural( grid.model_class ).lower() 
        
        __M_writer(u'\n')
        # SOURCE LINE 360
        if grid.use_paging and num_pages > 1:
            # SOURCE LINE 361
            __M_writer(u'        <tr id="page-links-row">\n')
            # SOURCE LINE 362
            if show_item_checkboxes:
                # SOURCE LINE 363
                __M_writer(u'                <td></td>\n')
                pass
            # SOURCE LINE 365
            __M_writer(u'            <td colspan="100">\n                <span id=\'page-link-container\'>\n')
            # SOURCE LINE 368
            __M_writer(u'                    ')

                        #
                        # Set minimum & maximum page.
                        # 
            page_link_range = num_page_links/2
            
            # First pass on min page.
            min_page = cur_page_num - page_link_range
            if min_page >= 1:
                # Min page is fine.
                min_offset = 0
            else:
                # Min page is too low.
                min_page = 1
                min_offset = page_link_range - ( cur_page_num - min_page )
            
            # Set max page.
            max_range = page_link_range + min_offset
            max_page = cur_page_num + max_range
            if max_page <= num_pages:
                # Max page is fine.
                max_offset = 0
            else:
                # Max page is too high.
                max_page = num_pages
                # +1 to account for the +1 in the loop below.
                max_offset = max_range - ( max_page + 1 - cur_page_num )
            
            # Second and final pass on min page to add any unused 
            # offset from max to min.
            if max_offset != 0:
                min_page -= max_offset
                if min_page < 1:
                    min_page = 1
                                
            
            # SOURCE LINE 402
            __M_writer(u'\n                    Page:\n')
            # SOURCE LINE 404
            if min_page > 1:
                # SOURCE LINE 405
                __M_writer(u'                        <span class=\'page-link\' id="page-link-1"><a href="')
                __M_writer(unicode(url( page=1 )))
                __M_writer(u'" page_num="1">1</a></span> ...\n')
                pass
            # SOURCE LINE 407
            for page_index in range(min_page, max_page + 1):
                # SOURCE LINE 408
                if page_index == cur_page_num:
                    # SOURCE LINE 409
                    __M_writer(u'                            <span class=\'page-link inactive-link\' id="page-link-')
                    __M_writer(unicode(page_index))
                    __M_writer(u'">')
                    __M_writer(unicode(page_index))
                    __M_writer(u'</span>\n')
                    # SOURCE LINE 410
                else:
                    # SOURCE LINE 411
                    __M_writer(u'                            ')
                    args = { 'page' : page_index } 
                    
                    __M_writer(u'\n                            <span class=\'page-link\' id="page-link-')
                    # SOURCE LINE 412
                    __M_writer(unicode(page_index))
                    __M_writer(u'"><a href="')
                    __M_writer(unicode(url( args )))
                    __M_writer(u'" page_num=\'')
                    __M_writer(unicode(page_index))
                    __M_writer(u"'>")
                    __M_writer(unicode(page_index))
                    __M_writer(u'</a></span>\n')
                    pass
                pass
            # SOURCE LINE 415
            if max_page < num_pages:
                # SOURCE LINE 416
                __M_writer(u'                        ...\n                        <span class=\'page-link\' id="page-link-')
                # SOURCE LINE 417
                __M_writer(unicode(num_pages))
                __M_writer(u'"><a href="')
                __M_writer(unicode(url( page=num_pages )))
                __M_writer(u'" page_num="')
                __M_writer(unicode(num_pages))
                __M_writer(u'">')
                __M_writer(unicode(num_pages))
                __M_writer(u'</a></span>\n')
                pass
            # SOURCE LINE 419
            __M_writer(u'                </span>\n                \n')
            # SOURCE LINE 422
            __M_writer(u'                <span class=\'page-link\' id=\'show-all-link-span\'> | <a href="')
            __M_writer(unicode(url( page='all' )))
            __M_writer(u'" page_num="all">Show All</a></span>\n            </td>\n        </tr>    \n')
            pass
        # SOURCE LINE 427
        if show_item_checkboxes:
            # SOURCE LINE 428
            __M_writer(u'        <tr>\n')
            # SOURCE LINE 430
            __M_writer(u'            <input type="hidden" id="operation" name="operation" value="">\n            <td></td>\n            <td colspan="100">\n                For <span class="grid-selected-count"></span> selected ')
            # SOURCE LINE 433
            __M_writer(unicode(items_plural))
            __M_writer(u':\n')
            # SOURCE LINE 434
            for operation in grid.operations:
                # SOURCE LINE 435
                if operation.allow_multiple:
                    # SOURCE LINE 436
                    __M_writer(u'                        <input type="button" value="')
                    __M_writer(unicode(operation.label))
                    __M_writer(u'" class="action-button" onclick="submit_operation(this, \'')
                    __M_writer(unicode(operation.confirm))
                    __M_writer(u'\')">\n')
                    pass
                pass
            # SOURCE LINE 439
            __M_writer(u'            </td>\n        </tr>\n')
            pass
        # SOURCE LINE 442
        if len([o for o in grid.operations if o.global_operation]) > 0:
            # SOURCE LINE 443
            __M_writer(u'    <tr>\n        <td colspan="100">\n')
            # SOURCE LINE 445
            for operation in grid.operations:
                # SOURCE LINE 446
                if operation.global_operation:
                    # SOURCE LINE 447
                    __M_writer(u'                ')

                    link = operation.global_operation()
                    href = url( **link )
                                    
                    
                    # SOURCE LINE 450
                    __M_writer(u'\n                <a class="action-button" href="')
                    # SOURCE LINE 451
                    __M_writer(unicode(href))
                    __M_writer(u'">')
                    __M_writer(unicode(operation.label))
                    __M_writer(u'</a>\n')
                    pass
                pass
            # SOURCE LINE 454
            __M_writer(u'        </td>\n    </tr>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fae9c32a990')._populate(_import_ns, [u'render_message'])
        _mako_get_namespace(context, '__anon_0x7faecc5f5310')._populate(_import_ns, [u'get_class_plural'])
        _mako_get_namespace(context, '__anon_0x7fae9c32a590')._populate(_import_ns, [u'handle_refresh_frames'])
        _mako_get_namespace(context, '__anon_0x7fae9421f790')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 50
        __M_writer(u'\n   ')
        # SOURCE LINE 51
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n   ')
        # SOURCE LINE 52
        __M_writer(unicode(self.grid_javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


