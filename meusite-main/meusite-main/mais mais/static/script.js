document.addEventListener('DOMContentLoaded', function() {
    loadMembers();
    setupSmoothScroll();
    setupHeaderScroll();
});

function loadMembers() {
    const membersGrid = document.getElementById('membersGrid');
    membersGrid.innerHTML = '<div class="loading">Carregando membros...</div>';

    fetch('/api/members')
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro na rede');
            }
            return response.json();
        })
        .then(members => {
            membersGrid.innerHTML = '';

            if (members.length === 0) {
                membersGrid.innerHTML = '<p>Nenhum membro encontrado.</p>';
                return;
            }

            members.forEach(member => {
                const memberCard = createMemberCard(member);
                membersGrid.appendChild(memberCard);
            });
        })
        .catch(error => {
            console.error('Erro ao carregar membros:', error);
            membersGrid.innerHTML = 
                '<p>Erro ao carregar os membros do grupo. Verifique o console para mais detalhes.</p>';
        });
}

function createMemberCard(member) {
    const card = document.createElement('div');
    card.className = 'member-card';

    card.innerHTML = `
        <img src="${member.image}" alt="${member.name}" class="member-image" loading="lazy">
        <div class="member-info">
            <h3>${member.name}</h3>
            <span class="member-instrument">${member.instrument}</span>
            <p class="member-bio">${member.bio}</p>
        </div>
    `;

    return card;
}

function setupSmoothScroll() {
    const navLinks = document.querySelectorAll('#mainNavigation a[href^="#"]');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#home') {
                // Scroll para o topo
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
                return;
            }
            
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                const headerHeight = document.getElementById('header').offsetHeight;
                const targetPosition = targetSection.offsetTop - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

function setupHeaderScroll() {
    const header = document.getElementById('header');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 100) {
            header.style.background = 'rgba(44, 62, 80, 0.95)';
            header.style.backdropFilter = 'blur(10px)';
        } else {
            header.style.background = '#2c3e50';
            header.style.backdropFilter = 'none';
        }
    });
}