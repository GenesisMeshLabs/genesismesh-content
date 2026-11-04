"""Generate covers for the eighteen additional portable-trust research articles.

Requires explicit selection; existing six article covers are not included.
Examples:
    python videos/scripts/generate_research_thumbnails.py --idea 2 3
    python videos/scripts/generate_research_thumbnails.py --all

Uses the repository's established series generator and approved brand assets.
Outputs the campaign cover, its configured upload copy and public cover.json.
Generation is local and does not upload, publish or schedule anything.
Generated pixels must be visually reviewed before publication.
"""
from pathlib import Path
import argparse, hashlib, json, math, re
from PIL import Image, __version__ as pillow_version
import generate_series_thumbnails as g

ROOT = Path(__file__).resolve().parents[2]

PIN = '3ccf2dd7caaeb9d0521949c3e9f8d9c0786d21ad'
PANEL = (20, 20, 24, 245)
WHITE = (255, 255, 255, 255)
INK = (7, 8, 7, 255)

def text(draw, xy, label, size=27, colour=WHITE):
    draw.text(xy, label, font=g.font(size), fill=colour)

def centered(draw, xy, label, size=27, colour=WHITE):
    box = draw.textbbox((0, 0), label, font=g.font(size))
    text(draw, (xy[0]-(box[2]-box[0])/2, xy[1]-(box[3]-box[1])/2-box[1]), label, size, colour)

def line(draw, points, accent, width=5):
    draw.line(points, fill=accent+(255,), width=width, joint='curve')

def arrow(draw, start, end, accent, width=5):
    line(draw, (start, end), accent, width)
    ang=math.atan2(end[1]-start[1], end[0]-start[0])
    pts=[end]+[(end[0]-18*math.cos(ang+s),end[1]-18*math.sin(ang+s)) for s in (-.55,.55)]
    draw.polygon(pts, fill=accent+(255,))

def node(draw, xy, label, accent, radius=43):
    x,y=xy
    draw.ellipse((x-radius,y-radius,x+radius,y+radius), fill=PANEL, outline=accent+(255,), width=5)
    centered(draw,xy,label,29)

def card(draw, box, label, accent, size=27):
    draw.rounded_rectangle(box, 13, fill=PANEL, outline=accent+(255,), width=4)
    centered(draw,((box[0]+box[2])/2,(box[1]+box[3])/2),label,size)

def cross(draw, xy, accent, r=20):
    x,y=xy
    line(draw,(x-r,y-r,x+r,y+r),accent,7)
    line(draw,(x+r,y-r,x-r,y+r),accent,7)

def concept(draw):
    centered(draw,(1010,605),'CONCEPT',18,(160,165,165,255))

def revoke_path(draw,a,s):
    pts=[(1010,175),(865,335),(1155,335),(1010,510)]
    for u,v in ((0,1),(0,2),(1,3),(2,3)): line(draw,(pts[u],pts[v]),a)
    for p,label in zip(pts,('A','B','C','D')):node(draw,p,label,a)
    cross(draw,(1083,247),(255,128,102),22)
    concept(draw)

def decision(draw,a,s):
    card(draw,(835,145,1185,245),'PROPOSAL',a,32)
    arrow(draw,(1010,257),(1010,315),a)
    line(draw,(810,335,1210,335),(255,255,255),5)
    card(draw,(835,385,1185,500),'POLICY',a,38)
    centered(draw,(1010,550),'?',55,a+(255,))
    concept(draw)

def missing(draw,a,s):
    for i,label in enumerate(('1','2','?','4')):
        y=150+i*100
        draw.rounded_rectangle((850,y,1170,y+75),13,fill=PANEL,outline=a+(255,),width=4)
        centered(draw,(895,y+37),label,35)
        if i!=2:line(draw,(930,y+37,1120,y+37),a,8)
        else:draw.rectangle((925,y+20,1130,y+55),outline=WHITE,width=3)
    concept(draw)

def hops(draw,a,s):
    for y,label in ((180,'MCP'),(345,'A2A'),(510,'HTTP')):
        card(draw,(890,y-45,1130,y+45),label,a,38)
    for y in (255,420):
        arrow(draw,(1010,y-20),(1010,y+35),a)
        line(draw,(820,y+8,950,y+8),(255,255,255),3)
        line(draw,(1070,y+8,1200,y+8),(255,255,255),3)
    concept(draw)

def compromise(draw,a,s):
    node(draw,(1010,180),'ACTOR',a,65)
    cross(draw,(1070,125),(255,128,102),20)
    arrow(draw,(1010,260),(1010,340),a)
    centered(draw,(1060,302),'?',40)
    draw.rounded_rectangle((825,375,1195,550),16,outline=WHITE,width=5)
    card(draw,(875,420,1145,505),'RESOURCE',a,31)
    concept(draw)

def reputation(draw,a,s):
    # A star is feedback, not a verified permission stamp.
    points=[]
    for i in range(10):
        r=95 if i%2==0 else 42;ang=-math.pi/2+i*math.pi/5
        points.append((1010+math.cos(ang)*r,245+math.sin(ang)*r))
    draw.polygon(points,outline=a+(255,),fill=PANEL)
    draw.line(points+[points[0]],fill=a+(255,),width=5,joint='curve')
    centered(draw,(1010,390),'IS NOT',32)
    card(draw,(840,455,1180,545),'PERMISSION',a,31)
    concept(draw)

def move(draw,a,s):
    card(draw,(855,150,1165,255),'IDENTITY',a,34)
    for x,y,label in ((855,455,'EDGE'),(1165,455,'CLOUD')):
        card(draw,(x-64,y-47,x+64,y+47),label,a,22)
        line(draw,(1010,270,x,y-60),a,4)
    arrow(draw,(935,455),(1085,455),(255,255,255))
    centered(draw,(1010,545),'NEW ADDRESS',24)
    concept(draw)

def accountable(draw,a,s):
    for i,label in enumerate(('IDENTITY','POLICY','ACTION','EVIDENCE')):
        y=125+i*115
        card(draw,(850,y,1170,y+78),label,a,29)
        if i<3:arrow(draw,(1010,y+83),(1010,y+106),a,4)
    concept(draw)

def member(draw,a,s):
    ctr=(1010,335);others=[(850,185),(1170,185),(850,490),(1170,490)]
    for p in others:line(draw,(ctr,p),a,4)
    node(draw,ctr,'TEAM',a,60)
    for i,p in enumerate(others):node(draw,p,str(i+1),a,42)
    cross(draw,(1170,490),(255,128,102),30)
    concept(draw)

def claims(draw,a,s):
    draw.rounded_rectangle((830,140,1190,280),22,fill=PANEL,outline=a+(255,),width=5)
    draw.polygon(((885,280),(885,315),(930,280)),fill=PANEL,outline=a+(255,))
    draw.line(((885,280),(885,315),(930,280)),fill=a+(255,),width=5,joint='curve')
    centered(draw,(1010,210),'"I AM..."',39)
    arrow(draw,(1010,325),(1010,380),a)
    card(draw,(865,415,1155,535),'PROOF?',a,43)
    concept(draw)

def disclosure(draw,a,s):
    draw.rounded_rectangle((850,155,1170,535),18,fill=PANEL,outline=a+(255,),width=5)
    for y,label in ((220,'NAME'),(325,'ISSUER'),(430,'SCOPE')):
        text(draw,(885,y),label,31)
        line(draw,(885,y+46,1125,y+46),a,3)
    draw.ellipse((870,306,1148,381),outline=WHITE,width=5)
    concept(draw)

def status_privacy(draw,a,s):
    card(draw,(835,145,1185,245),'STATUS FEED',a,29)
    for i in range(3):
        y=305+i*85;line(draw,(870,y,1150,y),a,8)
        draw.ellipse((830,y-10,850,y+10),fill=WHITE)
    draw.ellipse((925,505,1095,565),outline=WHITE,width=5)
    draw.ellipse((990,518,1030,552),fill=a+(255,))
    concept(draw)

def same_agent(draw,a,s):
    card(draw,(850,135,1170,225),'IDENTITY',a,34)
    arrow(draw,(1010,240),(1010,290),a)
    card(draw,(805,330,995,465),'BEFORE',a,27)
    card(draw,(1025,330,1215,465),'AFTER',a,27)
    centered(draw,(1010,535),'SAME?',42)
    concept(draw)

def telecom(draw,a,s):
    # Independent domains, with an unresolved crossing, not a deployed network.
    draw.rounded_rectangle((805,160,990,520),14,outline=a+(255,),width=5)
    draw.rounded_rectangle((1030,160,1215,520),14,outline=WHITE,width=5)
    centered(draw,(897,210),'DOMAIN A',22)
    centered(draw,(1122,210),'DOMAIN B',22)
    for x in (897,1122):
        line(draw,(x,330,x,460),a,6)
        draw.ellipse((x-15,300,x+15,330),fill=a+(255,))
        draw.arc((x-47,267,x+47,360),200,340,fill=a+(255,),width=4)
        draw.arc((x-68,246,x+68,382),200,340,fill=a+(255,),width=4)
    centered(draw,(1010,570),'WHO DECIDES?',27)
    concept(draw)

def car_mandate(draw,a,s):
    card(draw,(840,135,1180,245),'OWNER MANDATE',a,28)
    arrow(draw,(1010,265),(1010,325),a)
    draw.rounded_rectangle((840,410,1180,510),18,outline=WHITE,width=6,fill=PANEL)
    draw.polygon(((875,410),(920,345),(1100,345),(1145,410)),outline=a+(255,),fill=PANEL)
    draw.line(((875,410),(920,345),(1100,345),(1145,410)),fill=a+(255,),width=5,joint='curve')
    for x in (895,1125):draw.ellipse((x-28,480,x+28,536),fill=INK,outline=a+(255,),width=5)
    concept(draw)

def paid(draw,a,s):
    card(draw,(825,150,1195,285),'PAYMENT',a,40)
    centered(draw,(1010,345),'?',63)
    card(draw,(825,425,1195,560),'PERMISSION',a,35)
    concept(draw)

def offline_payment(draw,a,s):
    node(draw,(1010,170),'NA',a,55)
    for y in (240,265,290,370,395):line(draw,(1010,y,1010,y+14),a,5)
    cross(draw,(1010,335),(255,255,255),20)
    card(draw,(825,440,1195,540),'LOCAL PROOF?',a,34)
    concept(draw)

def minimum(draw,a,s):
    draw.rounded_rectangle((845,145,1175,545),18,fill=PANEL,outline=a+(255,),width=5)
    for y in (210,290,370,450):line(draw,(885,y,1135,y),a,8)
    draw.rounded_rectangle((868,266,1152,314),10,outline=WHITE,width=5)
    centered(draw,(1010,575),'WHICH FIELDS?',24)
    concept(draw)

SPECS = [
 (2,'governed','WHICH PATH\nWAS REVOKED?',revoke_path,'A conceptual four-node delegation graph with one crossed path asks which delegation was revoked; it does not claim graph-preserving revocation support.'),
 (3,'policy','WHO GETS\nTO DECIDE?',decision,'A proposal sits above a distinct policy boundary, asking who decides whether an action is authorized.'),
 (5,'policy',"WHAT'S\nMISSING?",missing,'Numbered evidence rows include a visible gap, asking what a signed audit history may leave out.'),
 (6,'running','LIMITS AT\nEVERY HOP',hops,'MCP, A2A and HTTP boxes cross separate boundaries, illustrating the need to preserve and recheck limits at each handoff.'),
 (7,'governed','ASSUME\nCOMPROMISE',compromise,'A marked actor approaches a resource boundary through a question mark; the illustration asks what remains protected after compromise.'),
 (8,'policy','REPUTATION\nIS NOT\nPERMISSION',reputation,'A feedback star and a permission card are separated by the words IS NOT, distinguishing reputation from authorization.'),
 (11,'running','IDENTITY\nON THE MOVE',move,'One identity connects to edge and cloud endpoints while the address changes; the illustration does not claim automatic migration.'),
 (14,'policy','WHO DID\nWHAT?',accountable,'A conceptual sequence distinguishes identity, policy, action and evidence in an accountable interaction.'),
 (15,'governed','ONE MEMBER\nCOMPROMISED',member,'A small team graph has one crossed member, asking how delegated scope changes the impact of compromise.'),
 (16,'policy','CLAIMS\nNEED PROOF',claims,'A speech bubble saying I AM leads to a proof question, distinguishing a conversational claim from verified identity.'),
 (17,'policy','WHAT DOES\nID REVEAL?',disclosure,'A credential card names NAME, ISSUER and SCOPE; the issuer field is highlighted to ask what identifying information is disclosed.'),
 (18,'policy','WHO CAN SEE\nREVOCATION?',status_privacy,'A status feed and an observing eye illustrate the privacy question raised by credential-status checks.'),
 (19,'running','SAME ID.\nSAME AGENT?',same_agent,'One identity points to before and after states, asking whether persistent identity proves continuity of current behavior.'),
 (20,'edge','WHO TRUSTS\nWHOM?',telecom,'Two independently outlined network domains illustrate cross-domain authorization as a design question, not a deployed 6G system.'),
 (21,'governed','WHO ALLOWED\nTHE PAYMENT?',car_mandate,'An owner mandate points toward a car, illustrating bounded machine-payment authority, not an implemented payment network.'),
 (22,'governed','PAID.\nAUTHORIZED?',paid,'Payment and permission appear in separate panels joined by a question mark, asking whether a settled payment matched the mandate.'),
 (23,'edge',"OFFLINE.\nWHAT'S PROVEN?",offline_payment,'A broken link separates an authority from a local-proof question, illustrating offline authorization limits without promising payment settlement.'),
 (24,'policy','HOW MUCH\nMUST YOU\nREVEAL?',minimum,'A document highlights one of several fields, asking which information is necessary without claiming anonymity or a zero-knowledge implementation.'),
]


FOLDERS = {2: 'campaigns/19-portable-trust-research/07-delegation-revocation', 3: 'campaigns/19-portable-trust-research/08-reasoning-and-authority', 5: 'campaigns/19-portable-trust-research/09-audit-completeness', 6: 'campaigns/19-portable-trust-research/10-cross-system-limits', 7: 'campaigns/19-portable-trust-research/11-compromised-agent', 8: 'campaigns/19-portable-trust-research/12-reputation-and-permission', 11: 'campaigns/19-portable-trust-research/13-identity-mobility', 14: 'campaigns/19-portable-trust-research/14-interaction-accountability', 15: 'campaigns/19-portable-trust-research/15-swarm-containment', 16: 'campaigns/19-portable-trust-research/16-identity-checks', 17: 'campaigns/19-portable-trust-research/17-issuer-privacy', 18: 'campaigns/19-portable-trust-research/18-revocation-privacy', 19: 'campaigns/19-portable-trust-research/19-identity-continuity', 20: 'campaigns/19-portable-trust-research/20-cross-domain-6g', 21: 'campaigns/19-portable-trust-research/21-vehicle-mandates', 22: 'campaigns/19-portable-trust-research/22-purchase-binding', 23: 'campaigns/19-portable-trust-research/23-offline-payments', 24: 'campaigns/19-portable-trust-research/24-payment-disclosure'}

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def checked_target(idea):
    folder = (ROOT / FOLDERS[idea]).resolve()
    campaign_root = (ROOT / 'campaigns').resolve()
    if not folder.is_relative_to(campaign_root) or not folder.is_dir():
        raise ValueError(f'Missing campaign folder for idea {idea}: {FOLDERS[idea]}')
    campaign_path = folder / 'campaign.json'
    campaign = json.loads(campaign_path.read_text(encoding='utf-8'))
    slug = campaign.get('slug', '')
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug):
        raise ValueError(f'Idea {idea} needs a plain lowercase hyphenated slug')
    configured = campaign.get('thumbnail')
    if not isinstance(configured, str) or not configured:
        raise ValueError(f'Idea {idea} is missing campaign.json thumbnail')
    upload = (folder / configured).resolve()
    expected = (ROOT / 'videos' / 'thumbnails' / f'{slug}.png').resolve()
    if upload != expected:
        raise ValueError(f'Idea {idea} thumbnail must resolve to videos/thumbnails/{slug}.png')
    return folder, upload

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument('--idea', type=int, nargs='+', choices=sorted(FOLDERS),
                           help='Original research idea IDs; existing six are excluded')
    selection.add_argument('--all', action='store_true', help='Explicitly regenerate all eighteen new research covers')
    args = parser.parse_args(argv)
    ids = sorted(FOLDERS) if args.all else sorted(set(args.idea))
    # Resolve every target before any writes, preventing partial runs on invalid metadata.
    targets = {idea: checked_target(idea) for idea in ids}
    specs = {row[0]: row for row in SPECS}
    font_path = Path(g.font(32).path)
    if not font_path.is_file():
        raise ValueError('A real outline font is required; bitmap fallback is not acceptable')
    for idea in ids:
        _, group, hook, motif, alt = specs[idea]
        _, accent, background = g.GROUPS[group]
        g.GROUPS[group] = ('PORTABLE TRUST /', accent, background)
        g.MOTIFS[motif.__name__] = motif
        folder, upload = targets[idea]
        cover = folder / 'thumbnail.png'
        g.make(f'idea-{idea:02d}', group, f'IDEA {idea:02d}', hook, motif.__name__, out=cover)
        with Image.open(cover) as image:
            if image.size != (1280, 720) or image.mode != 'RGB':
                raise ValueError(f'Unexpected cover format for idea {idea}')
        upload.parent.mkdir(parents=True, exist_ok=True)
        upload.write_bytes(cover.read_bytes())
        metadata = {
            'idea_id': idea,
            'series_label': f'PORTABLE TRUST / IDEA {idea:02d}',
            'hook': hook,
            'motif': motif.__name__,
            'motif_scope': 'Conceptual illustration, not product output or a claim of research implementation',
            'alt_text': alt,
            'cover': 'thumbnail.png',
            'upload_copy': upload.relative_to(ROOT).as_posix(),
            'sha256': sha(cover),
            'upload_sha256': sha(upload),
            'dimensions': [1280, 720],
            'mode': 'RGB',
            'accent_rgb': list(accent),
            'font': {'name': font_path.name, 'sha256': sha(font_path)},
            'pillow_version': pillow_version,
            'template_source_commit': PIN,
            'generator': 'videos/scripts/generate_research_thumbnails.py',
            'generator_sha256': sha(__file__),
            'assets': [{'path': path.relative_to(ROOT).as_posix(), 'sha256': sha(path)}
                       for path in (g.LOGO, background)],
            'visual_review': 'Regenerated asset: actual-pixel review required before publication',
        }
        (folder / 'cover.json').write_text(json.dumps(metadata, indent=2)+'\n', encoding='utf-8')
        print(cover.relative_to(ROOT).as_posix())
        print(upload.relative_to(ROOT).as_posix())

if __name__ == '__main__':
    main()
