A LaTeX-powered document generator web application for OpenShift based
on the [`diy` cartridge](http://openshift.github.io/documentation/oo_cartridge_guide.html#diy).

### Installation ###

* Create a [Do-It-Yourself 0.1](https://openshift.redhat.com/app/console/application_type/cart!diy-0.1) cartridge on OpenShift without adding a source code git repository (yet). You will have to add the code from this repository later because the OpenShift web console will time out if we add it now.

* Clone the app's repository from OpenShift using the `git URL` given in the web console after creating your app.

 ...**git clone** `git URL`

* Load the code from this repository into your app by running the following commands:

 ...**cd** `App Name`
 ...**git remote add upstream -m master** https://github.com/sjgardiner/openshift_diy_latex.git
 ...**git pull -s recursive -X theirs upstream master**

* Your repository will now match this one. The final step is to push the changes to OpenShift:

 ...**git push origin master**

* Sit back and relax. The app will automatically install Python and TeX Live on your OpenShift gear, so the first git push operation will take a long time. After it completes, your new app is ready to use.
