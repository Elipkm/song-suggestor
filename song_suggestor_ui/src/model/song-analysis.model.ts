

export const MOCK_ANALYSE = ['Love and loss, longing, emotional connection.', 'Nostalgia, yearning, melancholy.', 'A reflective lover, seeking understanding.', 'First-person perspective.', 'The complexity of love and its aftermath.', 'Ambiguously hopeful yet resigned.', 'Poetic and intimate language.', 'Melancholic yet tender tone.', 'Love, heartbreak, longing for belonging.'];


export class SongAnalysis {

    analysis: string[] = []

    constructor(analysis: string[]) {
        this.analysis = analysis
    }
}