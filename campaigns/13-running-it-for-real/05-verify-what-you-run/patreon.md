# Verify What You Run

**Running It for Real · Part 5 of 5**

*The program that holds a sovereign's signing key should be the first thing its operator can verify.*

An operator is about to deploy the program that will sign every treaty, decision and revocation it issues. It pulls an image by a familiar tag. What is inside? Who built it, and from what source? Is it the same image the tag pointed to yesterday?

The one program that will hold the sovereign's signing key is often the one thing nobody verified.

Our article on supply-chain trust drew a line between two layers. The artifact layer asks what was built and whether it was tampered with. The trust layer asks who was authorized to produce it. Genesis Mesh works on the second, but it has no standing to ask others for rigor it skips on the first. So it holds its own delivery to that standard.

The Network Authority, the service each operator runs to hold its keys and sign its trust decisions, ships as a published image for both common processor architectures, and so does the gateway in front of it. Each image carries a software bill of materials listing what is inside, and a provenance record of how it was built. Each is signed through Sigstore, a public signing service, with no long-lived key to steal: the signature binds the image to the project's release workflow at one exact tag and is recorded in a public transparency log. An operator who checks against that workflow identity gets a hard answer: either that workflow signed that image, or verification fails. An unsigned image is not a release.

Order matters too. Each image is built, scanned and tested, then pushed by its digest, its content fingerprint, with no tag. The pushed layers are checked against the ones that passed, the second architecture is scanned and tested, and only then is the image signed and tagged. A version tag is published once and never moved. An operator should resolve a tag to its digest, verify the signature on that digest and deploy that digest, so that what runs is exactly what was verified.

Inside, the authority image is kept small. It runs as a non-root user, installs only the package, its hash-locked Python dependencies, an init process and a shell, removes the Python package installer, holds no key material, and must pass a vulnerability gate that blocks any critical or high finding. Every operator runs the same verified image and supplies its own keys when the container starts. The software is shared. The sovereignty is not.

Developers get the same discipline. After installing the package, three commands start a local authority on a development server, built from the same application code and governance settings as production, so a controller meets the rules it will meet later, whichever SDK it is written with.

Trust in what an authority signs begins with being able to check what the authority is.

**Builds on our video** Supply Chain Trust: Beyond Artifact Signing: https://www.youtube.com/watch?v=H41w_3mMrcE

**Go deeper:**

Container images: https://docs.genesismesh.org/operations/container-images.html
A local Network Authority: https://docs.genesismesh.org/sdk/local-network-authority.html

**Next:** Lost, Misread or Erased

---

Genesis Mesh is a portable trust layer for sovereign systems, and it is open source.

Website: https://genesismesh.org
Documentation: https://docs.genesismesh.org
Live demo: https://mesh.genesismesh.org
GitHub: https://github.com/GenesisMeshLabs
