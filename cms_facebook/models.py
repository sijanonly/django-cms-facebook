from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


LAYOUT_CHOICES = [
    ('standard', _('standard')),
    ('button_count', _('button count')),
]

VERB_CHOICES = [
    ('like', _('like')),
    ('recommend', _('recommend')),
]

FONT_CHOICES = [
    ('arial', _('Arial')),
    ('lucida+grande', _('lucida grande')),
    ('segoe+ui', _('segoe ui')),
    ('tahoma', _('tahoma')),
    ('trebuchet+ms', _('trebuchet ms')),
    ('verdana', _('verdana')),
]

COLOR_CHOICES = [
    ('light', _('light')),
    ('dark', _('dark')),
]

SHARE_BUTTON_STYLES = (
    ('button', 'Simple "share" button'),
    ('button_count', 'Share button with count'),
    ('box_count', 'Share button with count displayed above'),
)


class ShareButton(CMSPlugin):
    style = models.CharField(max_length=12,choices=SHARE_BUTTON_STYLES)
    share_url = models.URLField(_("URL to share"), help_text=_("If blank, the page where it's displayed will be used"), 
                                null=True, blank=True)
    button_text = models.CharField(_("Button text"),help_text=_("This text will be displayed in the \"Share\" button"),
                                   max_length=255,default=_("Share"))

class LikeBox(CMSPlugin):
    pageurl = models.URLField(_("URL to like"))
    width = models.PositiveSmallIntegerField(_("Width"), default=None, null=True,
        blank=True, help_text=_("Leave empty for auto scaling"))
    height = models.PositiveSmallIntegerField(_("Height"), default=587)
    connections = models.PositiveSmallIntegerField(_("Amount of Users"), default=10)
    stream = models.BooleanField(_("Show stream"), default=True)
    header = models.BooleanField(_("Show header"), default=True)
    
    fb_bits = [
        'id',
        'connections',
        'stream',
        'header',
    ]
    
    fb_aliases = {
        'id': lambda r,c,i: i.fbpage.pageid,
    }
    
    fb_default_width = 295

    def __unicode__(self):
        return "LikeBox (%s)" % (self.pageurl)
    
    
class LikeButton(CMSPlugin):
    pageurl = models.URLField(_("URL to like"))
    layout = models.CharField(_("Layout Style"), choices=LAYOUT_CHOICES, default="standard", max_length=50)
    show_faces = models.BooleanField(_("Show Faces"), default=True,
        help_text=_("Show profile pictures below the like button"))
    width = models.PositiveSmallIntegerField(_("Width"), default=None, null=True,
        blank=True, help_text=_("Leave empty for auto scaling"))
    height = models.PositiveSmallIntegerField(_("Height"), default=80)
    verb = models.CharField(_("Verb to display"), choices=VERB_CHOICES, default='like', max_length=50)
    font = models.CharField(_("Font"), choices=FONT_CHOICES, default='verdana', max_length=50)
    color_scheme = models.CharField(_("Color Scheme"), choices=COLOR_CHOICES, default='light', max_length=50)
    
    fb_bits = [
        'href',
        'layout',
        'show_faces',
        'verb',
        'font',
        'color_scheme',
    ]
    
    fb_aliases = {
        'href': lambda r,c,i: i.url if i.url else r.build_absolute_uri(),
    }
    
    fb_default_width = 295

    def __unicode__(self):
        return "LikeButton (%s)" % (self.pageurl)