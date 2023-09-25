from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        host_Chile = self.addHost( 'h1' )
        host_Australia = self.addHost( 'h2' )

        Switch1 = self.addSwitch( 's1' )
        Switch2 = self.addSwitch( 's2' )
        Switch3 = self.addSwitch( 's3' )
        Switch4 = self.addSwitch( 's4' )

        # Add links
        self.addLink(host_Chile, Switch1)
        self.addLink(host_Australia, Switch4)
        
        self.addLink( Switch1, Switch2, bw=250, delay='150ms', loss=5)# especial
        self.addLink( Switch2, Switch3, bw=100, delay='70ms', loss=4)        
        self.addLink( Switch3, Switch4, bw=150, delay='200ms', loss=3)# Especial


topos = { 'mytopo': ( lambda: MyTopo() ) }

