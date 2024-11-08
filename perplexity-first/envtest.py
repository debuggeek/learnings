import sys
import pkg_resources

installed_packages = pkg_resources.working_set
package_names = [package.project_name for package in installed_packages]

print('perplexityai' in package_names, sys.executable)
