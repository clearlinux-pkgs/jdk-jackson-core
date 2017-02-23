Name     : jdk-jackson-core
Version  : 2.7.6
Release  : 2
URL      : https://github.com/FasterXML/jackson-core/archive/jackson-core-2.7.6.tar.gz
Source0  : https://github.com/FasterXML/jackson-core/archive/jackson-core-2.7.6.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-jackson-core-data
BuildRequires : apache-ant
BuildRequires : apache-maven
BuildRequires : apache-maven2
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-apache-parent
BuildRequires : jdk-aqute-bndlib
BuildRequires : jdk-atinject
BuildRequires : jdk-bsh
BuildRequires : jdk-build-helper-maven-plugin
BuildRequires : jdk-cdi-api
BuildRequires : jdk-cglib
BuildRequires : jdk-commons-beanutils
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-collections
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-digester
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-commons-validator
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-integration-tools
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-easymock3
BuildRequires : jdk-eclipse-eclipse
BuildRequires : jdk-eclipse-osgi
BuildRequires : jdk-eclipse-osgi-services
BuildRequires : jdk-fasterxml-oss-parent
BuildRequires : jdk-felix
BuildRequires : jdk-felix-bundlerepository
BuildRequires : jdk-felix-framework
BuildRequires : jdk-felix-osgi-foundation
BuildRequires : jdk-felix-utils
BuildRequires : jdk-glassfish-servlet-api
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-hamcrest
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jackson-parent
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-junit4
BuildRequires : jdk-kxml
BuildRequires : jdk-log4j
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-bundle-plugin
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-maven-dependency-tree
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-reporting-exec
BuildRequires : jdk-maven-reporting-impl
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-shared-incremental
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-maven-site-plugin
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-objenesis
BuildRequires : jdk-osgi-compendium
BuildRequires : jdk-osgi-core
BuildRequires : jdk-parboiled
BuildRequires : jdk-pegdown
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-compiler
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-replacer
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-snappy
BuildRequires : jdk-surefire
BuildRequires : jdk-velocity
BuildRequires : jdk-wagon
BuildRequires : jdk-xbean
BuildRequires : jdk-xerces-j2
BuildRequires : jdk-xml-apis
BuildRequires : jdk-xmlunit
BuildRequires : jdk-xz
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn

%description
# Overview
This project contains core low-level incremental ("streaming") parser and generator abstractions used by
[Jackson Data Processor](http://wiki.fasterxml.com/JacksonHome).
It also includes the default implementation of handler types (parser, generator) that handle JSON format.
The core abstractions are not JSON specific, although naming does contain 'JSON' in many places, due to historical reasons. Only packages that specifically contain word 'json' are JSON-specific.

%package data
Summary: data components for the jdk-jackson-core package.
Group: Data

%description data
data components for the jdk-jackson-core package.


%prep
%setup -q -n jackson-core-jackson-core-2.7.6

python3 /usr/share/java-utils/pom_editor.py pom_xpath_remove   "pom:reporting/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration"
python3 /usr/share/java-utils/pom_editor.py pom_xpath_inject   "pom:reporting/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']" '
<configuration>
<encoding>${project.reporting.outputEncoding}</encoding>
<quiet>true</quiet>
<source>${javac.src.version}</source>
</configuration>'
python3 /usr/share/java-utils/pom_editor.py pom_xpath_remove   "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions"
cp -p src/main/resources/META-INF/LICENSE .
cp -p src/main/resources/META-INF/NOTICE .
python3 /usr/share/java-utils/mvn_file.py : jackson-core

%build
python3 /usr/share/java-utils/mvn_build.py -- -Dmaven.test.failure.ignore=true

%install
xmvn-install  -R .xmvn-reactor -n jackson-core -d %{buildroot}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/jackson-core.jar
/usr/share/maven-metadata/jackson-core.xml
/usr/share/maven-poms/jackson-core.pom
