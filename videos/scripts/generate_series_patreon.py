"""Write patreon.md for campaigns 10 to 16 from each article.md.

    python videos/scripts/generate_series_patreon.py

The article body is used as written. Around it, each group gets its own frame:
a series kicker, a one-line standfirst, links back to earlier videos, docs to
go deeper and the next post. Re-run after any article change.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "campaigns"
DOCS = "https://docs.genesismesh.org/"
YT = {
    "01": ("What Is Portable Trust?", "https://www.youtube.com/watch?v=fv1XebByCbE"),
    "02": ("Portable Trust Across Boundaries", "https://www.youtube.com/watch?v=y3GBM5h-RdY"),
    "03": ("Sovereign Systems: Trust Without Central Control", "https://www.youtube.com/watch?v=OS9rGqOMkHY"),
    "04": ("How to Revoke Trust With Proof", "https://www.youtube.com/watch?v=PVOfYM48DYo"),
    "05": ("Why Every Trust Decision Needs a Signed Record", "https://www.youtube.com/watch?v=gp5yqnNQdZI"),
    "06": ("Why Trust Protocols Need Interoperability", "https://www.youtube.com/watch?v=v4ORssb6nLw"),
    "07": ("Genesis Mesh Trust API and SDKs Overview", "https://www.youtube.com/watch?v=E2UQRM7c3Vo"),
    "edge": ("Edge Infrastructure Needs Portable Identity", "https://www.youtube.com/watch?v=J7OpYQy3ZkU"),
    "supply": ("Supply Chain Trust: Beyond Artifact Signing", "https://www.youtube.com/watch?v=H41w_3mMrcE"),
}

FOOTER = """---

Genesis Mesh is a portable trust layer for sovereign systems, and it is open source.

Website: https://genesismesh.org
Documentation: https://docs.genesismesh.org
Live demo: https://mesh.genesismesh.org
GitHub: https://github.com/GenesisMeshLabs
"""

GROUPS = {
    "12-policy-and-evidence": "Policy and Evidence",
    "13-running-it-for-real": "Running It for Real",
    "14-governed-changes": "Governed Changes",
    "15-trust-at-the-edge": "Trust at the Edge",
    "16-proof-not-promises": "Proof, Not Promises",
}

# folder -> dict(standfirst, previously, builds_on, docs, try_it, closing)
META = {
    "12-policy-and-evidence/01-policy-you-can-read": dict(
        standfirst="Why a signed decision should name the rules that produced it, and why those rules should be documents rather than code.",
        builds_on="03",
        docs=[("Declarative boundary policy", "examples/declarative-boundary-policy.html")],
    ),
    "12-policy-and-evidence/02-allowed-is-not-done": dict(
        standfirst="A decision says what was allowed. This post is about recording what was actually done.",
        builds_on="05",
        docs=[("The evidence store", "examples/evidence-store.html")],
    ),
    "13-running-it-for-real/01-a-front-door-not-an-authority": dict(
        standfirst="Forty services need answers from the authority. None of them needs access to it.",
        builds_on="07",
        docs=[("The Rust gateway", "concepts/rust-gateway.html")],
    ),
    "13-running-it-for-real/02-watch-trust-cross-a-boundary": dict(
        standfirst="Two independently signed sovereigns, live, with nothing to sign up for. What the demo proves, and what it does not.",
        builds_on="02",
        docs=[("How the public reference is run", "operations/public-reference-dashboard.html")],
        try_it=True,
    ),
    "13-running-it-for-real/03-staying-up-without-giving-up-the-keys": dict(
        standfirst="How an operator keeps its authority available without handing it, or its keys, to someone else.",
        builds_on="03",
        docs=[("High availability", "operations/high-availability.html")],
    ),
    "13-running-it-for-real/04-a-contract-that-holds": dict(
        standfirst="What a stability promise has to cover when the things it protects are signed records meant to last for years.",
        docs=[("The public contract", "reference/public-contract.html"), ("Exit and fork", "operators/exit-and-fork.html")],
    ),
    "13-running-it-for-real/05-verify-what-you-run": dict(
        standfirst="The program that holds a sovereign's signing key should be the first thing its operator can verify.",
        builds_on="supply",
        docs=[("Container images", "operations/container-images.html"), ("A local Network Authority", "sdk/local-network-authority.html")],
    ),
    "14-governed-changes/01-lost-misread-or-erased": dict(
        standfirst="Three quiet ways evidence fails: it gets lost, it gets read two ways, or it disappears.",
        builds_on="05",
        docs=[("Evidence anchors", "operations/evidence-anchors.html")],
    ),
    "14-governed-changes/02-changes-that-happen-anyway": dict(
        previously="evidence that survives an outage, means one thing everywhere and cannot vanish unnoticed.",
        docs=[("Out-of-band changes", "operations/out-of-band-changes.html")],
    ),
    "14-governed-changes/03-rotate-forward-never-back": dict(
        previously="changes made outside the process, observed and judged as of when they happened.",
        docs=[("Remediation and reviews", "operations/remediation-and-reviews.html")],
    ),
    "14-governed-changes/04-an-audit-that-doesnt-trust-the-audited": dict(
        previously="what happens to a change judged wrong: rotate forward, or a second person lets it stand.",
        builds_on="05",
        docs=[("Audit packs", "operations/audit-packs.html"), ("Independent verification", "operations/independent-verification.html")],
    ),
    "14-governed-changes/05-new-key-same-past": dict(
        previously="an audit pack that someone outside can verify offline, without trusting the operator.",
        docs=[("Key succession", "operations/key-succession.html")],
    ),
    "15-trust-at-the-edge/01-permission-before-the-link-goes-down": dict(
        standfirst="What a device may do while it is cut off should be decided before the link goes down.",
        builds_on="edge",
        docs=[("Pre-issued grants", "operations/grants.html")],
    ),
    "15-trust-at-the-edge/02-the-device-asks-first": dict(
        standfirst="A small program on the device that asks first, acts within limits and can be cut off in one step.",
        previously="grants that let a device act within limits set in advance while it is cut off.",
        docs=[("The edge agent", "operations/edge-agent.html")],
    ),
    "16-proof-not-promises/01-five-languages-one-verdict": dict(
        standfirst="We promised that any implementation would reach the same verdict. This is how that promise became a test.",
        builds_on="06",
        docs=[("Interoperability", "development/interoperability.html"), ("Canonical form", "reference/canonical-form.html")],
    ),
    "16-proof-not-promises/02-what-a-proof-proves": dict(
        standfirst="A claim our prover broke in six steps, and a proof that silently never ran.",
        docs=[("Formal verification", "examples/formal-verification.html")],
    ),
    "16-proof-not-promises/03-finding-our-own-flaws-first": dict(
        standfirst="The flaws we found in our own code, how they were fixed, and how we keep looking.",
        docs=[("Changelog", "changelog.html"), ("Security policy", "https://github.com/GenesisMeshLabs/genesismesh/blob/main/SECURITY.md")],
    ),
    "16-proof-not-promises/04-the-rules-cant-live-in-one-head": dict(
        standfirst="The engineering behind a trust layer, and why its rules cannot depend on one person's memory.",
        docs=[("Decision records", "development/decisions/index.html")],
        closing="This post closes the series. Thank you for reading along, and for supporting the work.",
    ),
}


def read(folder):
    text = (ROOT / folder / "article.md").read_text(encoding="utf-8").strip()
    title, _, body = text.partition("\n")
    return title.lstrip("# ").strip(), body.strip()


def link(path):
    return path if path.startswith("http") else DOCS + path


def series_folders():
    return sorted(str(p.parent.relative_to(ROOT)).replace("\\", "/")
                  for p in ROOT.glob("1[2-6]-*/*/article.md"))


def write(folder, text):
    (ROOT / folder / "patreon.md").write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")
    print("wrote", folder)


def opener(folders):
    title, body = read("11-after-the-signature")
    lines = [f"# {title}", "",
             "*A new series on what Genesis Mesh has become since our first posts, and why it matters.*", "",
             body, "", "**The series**", ""]
    for key, name in GROUPS.items():
        titles = [read(f)[0] for f in folders if f.startswith(key)]
        lines.append(f"{name}: " + " · ".join(titles))
        lines.append("")
    lines += [f"If you are new here, start with our first video, {YT['01'][0]}: {YT['01'][1]}", "", FOOTER]
    return "\n".join(lines)


def post(folder, folders):
    group = folder.split("/")[0]
    members = [f for f in folders if f.startswith(group + "/")]
    n, total = members.index(folder) + 1, len(members)
    meta = META[folder]
    title, body = read(folder)
    lines = [f"# {title}", "", f"**{GROUPS[group]} · Part {n} of {total}**", ""]
    if meta.get("standfirst"):
        lines += [f"*{meta['standfirst']}*", ""]
    if meta.get("previously"):
        lines += [f"Previously: {meta['previously']}", ""]
    lines += [body, ""]
    if meta.get("try_it"):
        lines += ["**Try it yourself:** https://mesh.genesismesh.org (no account needed)", ""]
    if meta.get("builds_on"):
        name, url = YT[meta["builds_on"]]
        lines += [f"**Builds on our video** {name}: {url}", ""]
    docs = meta.get("docs", [])
    if docs:
        label = "Check it yourself" if group.startswith("16") else "Go deeper"
        lines += [f"**{label}:**", ""] + [f"{name}: {link(p)}" for name, p in docs] + [""]
    index = folders.index(folder)
    if index + 1 < len(folders):
        lines += [f"**Next:** {read(folders[index + 1])[0]}", ""]
    if meta.get("closing"):
        lines += [meta["closing"], ""]
    lines.append(FOOTER)
    return "\n".join(lines)


def main():
    folders = series_folders()
    missing = set(folders) - set(META)
    if missing:
        raise SystemExit(f"no metadata for {sorted(missing)}")
    # 10 is already published: keep the published text as the post
    src = ROOT / "10-genesis-mesh-did-not-start-with-genesis-mesh" / "article.md"
    write("10-genesis-mesh-did-not-start-with-genesis-mesh", src.read_text(encoding="utf-8"))
    write("11-after-the-signature", opener(folders))
    for folder in folders:
        write(folder, post(folder, folders))


if __name__ == "__main__":
    main()
